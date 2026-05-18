# DSPy Mission Control

A hands-on intro to DSPy, themed around Houston Mission Control. Built for the PyHou meetup at Improving Houston, May 19 2026.

The notebook walks through DSPy in three thirds: signatures, modules, and optimizers. The hero moment is a live `BootstrapFewShot` optimization followed by a pre-compiled `MIPROv2` artifact, both of which let you see the prompts the library writes from your signature.

## Quick start

```
git clone https://github.com/ahliana/dspy_mission_control.git
cd dspy_mission_control
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
python scripts/setup.py
```

Then copy `.env.example` to `.env` and add your `ANTHROPIC_API_KEY`. Open `dspy_mission_control.ipynb` in Jupyter and run cells top to bottom.

## What is in here

| File | Purpose |
|---|---|
| `dspy_mission_control.ipynb` | The 28-cell walkthrough |
| `miprov2_artifact.json` | Pre-compiled MIPROv2 result loaded by cell 11 |
| `scripts/setup.py` | One-command environment setup with smoke test |
| `scripts/run_miprov2.py` | Regenerate the MIPROv2 artifact yourself (~5 to 30 min, under $3) |
| `requirements.txt` | Pinned dependencies |
| `.env.example` | Template for your `ANTHROPIC_API_KEY` |

## The notebook in three thirds

**Signatures (cells 1 to 6)**: the smallest signature, class-form signatures, and `dspy.inspect_history` which reveals the prompt DSPy wrote on your behalf.

**Modules (cells 7 to 9)**: `Predict` versus `ChainOfThought` side by side, a real code-reviewer module, and a one-line swap from Claude Haiku 4.5 to Sonnet 4.6.

**Optimizers (cells 10 to 11)**: live `BootstrapFewShot` that runs in under 90 seconds, then a pre-baked `MIPROv2` artifact for the more sophisticated reveal.

`dspy.inspect_history(n=1)` is the magic ingredient throughout. After every cell, it shows the prompt DSPy sent to the model. You will see prompts you never wrote, built from signatures you did.

## What to do next

Pick one and adapt:

- Build a meeting-notes summarizer using the patterns in cells 7 and 8
- Build a classifier for your own data with a metric function you write
- Take any prompt you currently hand-tune and rewrite it as a signature

The DSPy docs at https://dspy.ai have the full story on advanced optimizers, retrievers, and agents.

Built for PyHou at Improving, Houston.
