# TIMELINE.md

The 40-minute talk plus 10-minute Q&A, minute by minute. This is the contract.

## Overview

```
6:40 PM   ---  TALK BEGINS
6:40-6:43   Opening (3 min)
6:43-6:52   FIRST THIRD: Signatures - "declare" (9 min)
6:52-7:01   MIDDLE THIRD: Modules - "compose" (9 min)
7:01-7:11   FINAL THIRD: Optimizers - "tune" + beat-the-hand-tuned-prompt (10 min)
7:11-7:14   Debrief: repo, method, related tools, connection minute (3 min)
7:14-7:20   Lightning talk ask + closing thanks (6 min)
7:20-7:30   Q&A (10 min)
7:30 PM   ---  Q&A ENDS, lightning talks start
```

## Segment 1: Opening, 0:00 to 0:03 (6:40 to 6:43)

- Slide 1 up (title). Brief self-intro
- Slide 2 up (three QRs: PyHou Discord, my repo, my LinkedIn). Hold 30+ seconds
- Recording acknowledgment for TechTalk YouTube
- **The x-ray glasses tease**: "Tonight, you get x-ray glasses. Not for the LLM. For your own code. By the end of these 40 minutes you will see every prompt DSPy sent, every demonstration it picked, every instruction it rewrote. Then we beat a hand-written prompt on a metric, live. Twice. Let's go."

## Segment 2: FIRST THIRD - Signatures ("declare"), 0:03 to 0:12 (6:43 to 6:52)

The paradigm shift. Declaration over prompting. `inspect_history` first appears here.

| Time | Asset | Action |
|---|---|---|
| 0:03 | Slide 3 | "Who has hand-tuned a prompt for hours?" Show of hands |
| 0:04 | Slide 4 | The 5-character signature: `dspy.Predict("text -> sentiment: str")` |
| 0:04:30 | Cell 1 | Run setup |
| 0:05 | Cell 2 | Run the string signature |
| 0:05:30 | Cell 3 | **X-RAY GLASSES MOMENT 1**: `inspect_history` shows the actual prompt DSPy wrote |
| 0:06:30 | Cell 4 | Class-form signature with typed fields |
| 0:07:30 | Cell 5 | Absurd vibes demo (humor moment) |
| 0:08:30 | Slide 5 | Partner activity: write a signature on the index card |
| 0:08:45 | (timer) | 90-second timer |
| 0:10:15 | (collect) | Pass cards forward. Pick 2 for later. Save 1 for the audience vote in segment 4 |
| 0:11 | Cell 6 | Type one attendee's signature LIVE. Run it. NAME the author on screen |
| 0:12 | Transition | "Signatures say WHAT. Modules say HOW." |

**Note**: This third was 10 minutes in the old plan. It is now 9 minutes. Keep the partner activity at 90 seconds, not 2 minutes.

## Segment 3: MIDDLE THIRD - Modules ("compose"), 0:12 to 0:21 (6:52 to 7:01)

Composition and reusability. Second appearance of `inspect_history`.

| Time | Asset | Action |
|---|---|---|
| 0:12 | Slide 6 | Predict, ChainOfThought, ReAct |
| 0:13 | Cell 7 | Predict vs ChainOfThought side by side. Reasoning field appears automatically |
| 0:14 | Cell 7 | **X-RAY GLASSES MOMENT 2**: `inspect_history` on both. Show what CoT added |
| 0:15 | Cell 8 | Code reviewer module: quality score, issues, improved code |
| 0:17 | Cell 9 | Swap Haiku to Sonnet in ONE line. A/B compare outputs |
| 0:19 | (transition) | "Now the payoff. Optimizer time." |
| 0:20 | (lightning seed) | "Before the optimizer section: think about ONE thing you could teach in 5 minutes." |

**Note**: Was 10 min, now 9 min. If running long at 0:19, CUT the Sonnet swap in cell 9. The point still lands.

## Segment 4: FINAL THIRD - Optimizers ("tune") + BEAT THE HAND-TUNED PROMPT, 0:21 to 0:31 (7:01 to 7:11)

The centerpiece. This is where all five promises land. **10 minutes, protected.**

| Time | Asset | Action |
|---|---|---|
| 0:21 | Slide 7 | "The library writes better prompts than you do. I will prove it." |
| 0:21:30 | Cell 10 | Define `ClassifyTransmission` signature, training examples, metric |
| 0:22:30 | Cell 10 | Run baseline (plain Predict), then score it on the 10 tests (~60%, misses print on screen) |
| 0:22:45 | Cell 10 | **X-RAY GLASSES MOMENT 3**: `inspect_history` shows baseline prompt |
| 0:23 | Cell 11 | **THE HAND-TUNED PROMPT**: show a careful safety-first prompt for the same task. Evaluate it on 10 test examples. Show its accuracy (~60%, misses the unconfirmed-hazard cases) |
| 0:24:30 | Cell 11 | **X-RAY GLASSES MOMENT 4**: point at the "escalate unconfirmed hazards to urgent" rule. It over-escalates suspected cases the convention calls attention |
| 0:25 | Cell 12 | **LIVE BootstrapFewShot**. Compiles in a few seconds. Explain the mechanism before you run it, not during |
| 0:26:30 | Cell 12 | Optimizer done. Run on the same 10 test examples. Show accuracy (~90%, beats hand-tuned by ~30 points) |
| 0:27 | Cell 12 | **X-RAY GLASSES MOMENT 5**: `inspect_history` reveals demos DSPy added. Compare directly to hand-tuned prompt |
| 0:28 | (transition) | "BootstrapFewShot only picked examples. What if the optimizer rewrites the instruction too? That is MIPROv2." |
| 0:28:30 | Cell 12 (continued) | Load pre-compiled `miprov2_artifact.json`. Run on same 10 test examples. Scores 100% (60 / 90 / 100) |
| 0:29 | Cell 12 | **X-RAY GLASSES MOMENT 6**: `inspect_history` shows MIPROv2 wrote the convention out as an instruction (Confirmed = urgent, hedging = attention, past-tense = routine); the cell extracts it clean below the dump. Then the scoreboard chart: 60 / 60 / 90 / 100 |
| 0:29:30 | (audience) | Read the saved audience card. Show of hands. Winner gets typed into cell 6 live |
| 0:30 | Cell 6 (revisit) | Run the audience-voted use case. NAME the author on screen |
| 0:30:45 | (transition) | "Mission accomplished. Debrief." |

**This segment IS the description's promise.** Do not cut.

## Segment 5: Debrief, 0:31 to 0:34 (7:11 to 7:14)

- Slide 8 up
- Repo URL (large): `github.com/[handle]/dspy_starship`
- The **METHOD**: point at `METHOD.md` in the repo. "Everything you saw, in a workflow you can apply Monday morning."
- Related tools, one line each: Arize Phoenix, MCP, pydantic-ai, uv+ruff, Claude Code
- 60-second **connection minute**: turn right, trade LinkedIn, share one thing you want to build with DSPy

## Segment 6: Lightning ask + closing, 0:34 to 0:40 (7:14 to 7:20)

- Slide 9 up
- "The bar is lower than you think. 4 minutes plus 1 for questions. Sign up at the door."
- NAME the two index card authors from segment 2 and the audience-voted author from segment 4
- Slide 10 up (thank you)
- Thank Dillon, Danyal, Improving, PyTexas by name
- "Questions?"

## Segment 7: Q&A, 0:40 to 0:50 (7:20 to 7:30)

10 minutes. Repeat each question for the YouTube audience. See SPEAKER_NOTES for 5 seed questions if it stalls.

At 7:28: "One more question."
At 7:29:30: wrap.
At 7:30: "Thanks everyone. Repo is on the screen. Find me at the back. Lightning talks are up next."

## Critical timing watchouts

- **First third often runs long**. Keep partner activity at 90 seconds
- **Live BootstrapFewShot** compiles in a few seconds and is deterministic at temperature 0, so it is now low-risk. The ~90 seconds the old plan budgeted for the compile is freed. Spend it on Q&A or the connection minute
- **The demo ladder is 60 / 60 / 90 / 100** (plain baseline, hand-tuned, BootstrapFewShot, MIPROv2). Verified stable across runs at temperature 0. If a live number drifts by a point, the beat still holds
- **Q&A always runs long OR short**. Have 5 seed questions ready
- **The 10-minute optimizer third is the promise. Do not cut into it.**

## If running behind at 0:20

Cut Sonnet swap (cell 9). Save 2 min.

## If running behind at 0:29

Cut the MIPROv2 reveal (cell 12 second half). Save 2 min. BootstrapFewShot + hand-tuned beat is the core promise. MIPROv2 is the "look what a serious optimizer does" bonus.

## If running short

More Q&A. Feature not bug.
