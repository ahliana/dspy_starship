# The DSPy Method

**Your Monday morning workflow after tonight.**

Take any prompt you currently hand-tune. Turn it into a DSPy program in 8 steps.

## Step 1: Declare the signature

Write what goes in and what comes out. Do not write a prompt.

```python
class MyTask(dspy.Signature):
    """One-sentence description of the task."""
    input_field: str = dspy.InputField(desc="what this is")
    output_field: str = dspy.OutputField(desc="what you want back")
```

**Rule**: if you catch yourself writing "please" or "you are a helpful assistant" in the docstring, delete it. The signature is the specification, not the pitch.

## Step 2: Compose with a module

Pick one:

- `dspy.Predict` if the task is straightforward
- `dspy.ChainOfThought` if the model benefits from reasoning aloud
- `dspy.ReAct` if the model needs to call tools

```python
program = dspy.ChainOfThought(MyTask)
```

**Rule**: start with `Predict`. Upgrade to `ChainOfThought` only if the metric says it helps.

## Step 3: Collect 10 to 30 examples

Each example has inputs plus the right output. No labels needed if you can score outputs another way (LLM-as-judge, exact match, human eval).

```python
train = [
    dspy.Example(input_field="...", output_field="...").with_inputs("input_field"),
    # 10 to 30 more
]
```

**Rule**: use REAL data from your app. Not synthetic. Not hypothetical. Real.

## Step 4: Write a metric

A function that takes an example and a prediction and returns True/False (or a score 0.0-1.0).

```python
def my_metric(example, pred, trace=None):
    return example.output_field.strip().lower() == pred.output_field.strip().lower()
```

**Rule**: start with exact match. Upgrade to LLM-as-judge only when exact match cannot capture what you care about. The metric IS the game.

## Step 5: Split train and test

Hold out 20 to 30 percent as test. Do not let the optimizer see it.

```python
random.shuffle(examples)
train = examples[:int(0.7 * len(examples))]
test = examples[int(0.7 * len(examples)):]
```

**Rule**: if you skip this step, you are measuring memorization, not learning.

## Step 6: Optimize

Fast path:

```python
from dspy.teleprompt import BootstrapFewShot
optimizer = BootstrapFewShot(metric=my_metric, max_bootstrapped_demos=3)
optimized = optimizer.compile(student=program, trainset=train)
```

Slow path (better results). MIPROv2 needs the optional `optuna` package first: `pip install optuna`.

```python
from dspy.teleprompt import MIPROv2
miprov2 = MIPROv2(
    metric=my_metric,
    prompt_model=strong_lm,   # a stronger model writes the instruction candidates
    task_model=cheap_lm,      # the model you will actually run in production
    auto="medium",            # "heavy" for the final compile
    max_labeled_demos=16,     # keep demo budget up; tiny budgets drop demos entirely
    num_threads=8,
)
optimized = miprov2.compile(student=program, trainset=train, valset=val)
```

**Rule**: run BootstrapFewShot first. Move to MIPROv2 when the metric plateaus.

**Rule**: give MIPROv2 a separate valset and a real demo budget. If MIPROv2 scores WORSE than BootstrapFewShot, it almost certainly dropped its demonstrations during the search. Raise `max_labeled_demos`, add data, and re-run.

## Step 7: Measure and inspect

```python
correct = sum(my_metric(ex, optimized(**ex.inputs())) for ex in test)
print(f"Accuracy: {correct / len(test) * 100:.0f}%")

# See what the optimizer wrote
dspy.inspect_history(n=1)
```

**Rule**: always use `inspect_history()` after optimization. If you cannot explain what changed, you do not understand your program yet.

## Step 8: Save and deploy

```python
optimized.save("my_program.json")
```

In production:

```python
program = dspy.ChainOfThought(MyTask)
program.load("my_program.json")
result = program(input_field="new data")
```

**Rule**: version-control the artifact. Treat it like a model file, not a config.

## When the model provider releases a new model

1. Update the LM: `dspy.LM("anthropic/new-model-id")`
2. Re-run steps 6 and 7
3. Save a new artifact
4. A/B test against the old artifact

**Rule**: you are never rewriting a prompt again. You are re-running an optimizer.

## Common mistakes to avoid

- **Trying to skip the metric.** The metric is the whole game. Cheap metrics give you cheap programs.
- **Using too few examples.** BootstrapFewShot works with 5-20. MIPROv2 wants 20-200. Below the floor, the optimizer has nothing to work with.
- **Not looking at the compiled prompt.** `inspect_history` is not optional. If you skip it, you are back to prompt engineering by superstition.
- **Optimizing with the test set in your training data.** Please do not.
- **Assuming the optimizer will save you from a bad task definition.** If you cannot describe the task clearly to a smart intern, the signature will not save you.

## When to reach for DSPy

- You are iterating on prompts anyway
- You have or can build a metric
- You expect to swap models over time
- You want reviewable, version-controllable programs

## When NOT to reach for DSPy

- One-shot creative tasks with no metric ("write me a poem")
- Zero examples and no way to get any
- The hard part is orchestration, not prompt quality (in that case, LangChain or LlamaIndex, which coexist with DSPy)

That is the method.
