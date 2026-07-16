# CLAUDE.md

**Read this file completely before doing anything. Then read `TIMELINE.md`. Then wait for the user's go.**

**This is a 40-minute talk plus 10-minute Q&A. Total 50 minutes. NOT 15. NOT 30. Do not shorten.**

The previous Claude Code session rewrote this talk from 45 minutes to 15 minutes and removed MIPROv2. This wasted the user's Sunday. Do not do that. If you are tempted to "simplify" anything, stop and ask.

## What this project is

40-minute technical talk on DSPy at PyHou (Python Houston), Tuesday July 21, 2026 at Improving Houston. Speaker: Ahliana Byrd. Her name appears exactly that way; do not add any online handle or alias to the talk materials. Talk runs 6:40 to 7:20 PM, Q&A 7:20 to 7:30 PM.

Recorded for the TechTalk YouTube channel. Hosts: Dillon Niederhut, Danyal M. Sponsors: Improving, PyTexas.

## The submitted title, description, and bio are LOCKED

**Title**: From Crop Duster to Starship: Let DSPy Tune Your Prompts in Plain Python

**Description promises FIVE things that MUST ship:**
1. Declare + compose + optimize (the three DSPy primitives, in order, named)
2. X-ray glasses: `dspy.inspect_history()` as a running metaphor
3. Build the whole thing LIVE on stage
4. **Beat a hand-written prompt** on a measurable metric
5. Take-homes: a repo AND a method (workflow doc)

If any deliverable in this project drops one of those five, stop and flag it.

## The talk structure is LOCKED

| Time | Segment | Notebook | Slides |
|---|---|---|---|
| 0:00 to 0:03 | Opening, x-ray glasses tease | - | 1, 2 |
| 0:03 to 0:12 | 1st third: Signatures (declare) | Cells 1-6 | 3, 4, 5 |
| 0:12 to 0:21 | 2nd third: Modules (compose) | Cells 7-9 | 6 |
| 0:21 to 0:31 | 3rd third: Optimizers + beat-the-hand-tuned-prompt | Cells 10-12 | 7 |
| 0:31 to 0:34 | Debrief: repo, method, tools, connection minute | - | 8 |
| 0:34 to 0:40 | Lightning talk ask + closing | - | 9, 10 |
| 0:40 to 0:50 | Q&A (10 min) | - | 10 holds |

Full minute-by-minute breakdown in `TIMELINE.md`.

## File map

| File | Purpose |
|---|---|
| `CATCHUP.md` | User's summary to remember the project |
| `CLAUDE.md` | This file. Master instructions |
| `TIMELINE.md` | The 40+10 talk breakdown |
| `SPEAKER_NOTES.md` | What Ahliana will say |
| `dspy_starship_01.ipynb` | The notebook that IS the talk, walked through live |
| `slides.html` | The 10-slide deck, self-contained, opened in a browser tab |
| `METHOD.md` | The workflow write-up, promise 5's "method" take-home |
| `scripts/setup.py` | Environment setup, Python not bash |
| `scripts/run_miprov2.py` | Compiles MIPROv2 artifact (5-10 min, heavy mode), or BSRS fallback |
| `scripts/execute_notebook.py` | Runs the notebook end-to-end, saves offline backup |
| `requirements.txt` | Pinned dependencies |
| `.env.example` | Template; uncomment ANTHROPIC_API_KEY or OPENAI_API_KEY |
| `miprov2_artifact.json` | Compiled artifact, committed on purpose (synthetic data only) |
| `backups/full_demo.ipynb` | Offline fallback with all outputs preserved |

## Style preferences (NON-NEGOTIABLE)

- **No em dashes** anywhere
- **Python only**. You may RUN bash commands. You may not WRITE bash scripts. Setup scripts are Python.
- Markdown outlines for plans
- Direct and concise. No flattery. No excessive apology
- Complete sentences with explicit subjects. No participial fragments like "Looking forward to"
- Dates in filenames: `YYYYMMDD_HHmm_`
- No colons in filenames, alphanumeric + spaces + underscores only

## What you should do

Work one task at a time. Verify each before moving on. Do not batch.

### Task 1: Confirm you read this file and TIMELINE.md

Tell the user: "I read CLAUDE.md and TIMELINE.md. The talk is 40 minutes plus 10 minutes Q&A. The theme is Crop Duster to Starship. The five description promises are locked. I will not shorten or remove anything without permission. Which task do you want first?"

Wait for the user's response.

### Task 2: Environment setup

```
python scripts/setup.py
```

Expected: prints `SETUP COMPLETE`. If it does not, stop and report the exact error.

### Task 3: Confirm API key

The user needs to edit `.env` and set `ANTHROPIC_API_KEY` to their real key. Check `.env` exists and does not contain the placeholder. If placeholder or missing, tell the user once and wait.

### Task 4: Smoke test

Run this in Python to verify DSPy talks to Anthropic:

```python
import os
from dotenv import load_dotenv
import dspy
load_dotenv()
lm = dspy.LM("anthropic/claude-haiku-4-5-20251001", max_tokens=500)
dspy.configure(lm=lm)
r = dspy.Predict("question -> answer")(question="What year was DSPy released?")
print(r.answer)
```

If it prints an answer, DSPy works. If not, report the exact error.

### Task 5: Sunday-equivalent prep

```
python scripts/run_miprov2.py
```

Takes 5 to 10 minutes for MIPROv2 (heavy mode, Sonnet proposer, Haiku task model). If MIPROv2 errors, falls back to BootstrapFewShotWithRandomSearch (5 to 10 min). Produces `miprov2_artifact.json`. A compiled artifact already ships with the repo, so this is a rebuild step, not a prerequisite.

TELL the user how long it will take BEFORE starting. Let it run in the background.

### Task 6: Offline backup

```
python scripts/execute_notebook.py
```

Runs the notebook end-to-end, saves with outputs to `backups/full_demo.ipynb`. This is the fallback if live demo fails on stage. Takes 5 to 10 minutes.

### Task 7: Placeholder replacement

Replace `[your-handle]` in `README.md`, notebook markdown cells, and any other files. Ask the user for the handle once.

### Task 8: Final verification

Confirm these files exist and are non-empty:
- `dspy_starship_01.ipynb`
- `slides.html`
- `miprov2_artifact.json`
- `backups/full_demo.ipynb`
- `.env` (with real key)
- `CATCHUP.md`, `CLAUDE.md`, `TIMELINE.md`, `SPEAKER_NOTES.md`
- `requirements.txt`

Report status. Stop.

## What you must NEVER do without explicit user confirmation

- Shorten the talk
- Remove MIPROv2 or BootstrapFewShot
- Remove the beat-the-hand-tuned-prompt demo (cells 10-12)
- Remove any notebook cells
- Change the Crop Duster to Starship theme
- Push to GitHub
- Make git commits
- Modify `CATCHUP.md`, `CLAUDE.md`, `TIMELINE.md`, or `SPEAKER_NOTES.md`
- "Simplify" or "improve" any file the user did not ask you to change
- Run anything that costs more than $5 in API calls without warning

## What you should ALWAYS do

- Verify each step worked before the next
- Report exact error messages, not summaries
- Write Python, not bash
- Ask before any destructive change
- Tell the user how long a long-running operation will take BEFORE starting
- Assume the user is time-constrained. Do not add tasks she did not ask for.
