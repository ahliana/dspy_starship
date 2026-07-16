# DSPy Starship: Catchup Summary

Read this first. Everything you need to remember, on one page.

## The talk

- **What**: 40-minute talk on DSPy at PyHou (Python Houston), followed by 10 min Q&A
- **Where**: Improving Houston, 10111 Richmond Ave, Suite 100, Houston
- **When**: Tuesday July 21, 2026, 6:40 PM to 7:30 PM (talk 6:40 to 7:20, Q&A 7:20 to 7:30)
- **After you**: Lightning talks 7:30 to 8:00 (4 min + 1 min Q per speaker)
- **Recorded**: Yes, on the TechTalk YouTube channel
- **Hosts**: Dillon Niederhut and Danyal M.
- **Sponsors to thank**: Improving, PyTexas

## What was submitted to Dillon (LOCKED, do not change)

- **Title**: From Crop Duster to Starship: Let DSPy Tune Your Prompts in Plain Python
- **Description**: DSPy takes hand-tuned prompts (crop duster) and turns them into declared programs (starship). Declare, compose, optimize. X-ray glasses (`inspect_history`) show every move. Build live, beat a hand-written prompt, send home a repo and a method.
- **Bio**: Principal Software Engineer at Ascentra, Python/C#/Angular, hands-on with agentic AI, Johns Hopkins Advanced Agentic AI program

## Five specific promises from the description (must ship)

1. Declaration + composition + optimization (the three DSPy primitives)
2. X-ray glasses (`inspect_history` as running metaphor throughout)
3. Build the whole thing LIVE on stage
4. **Beat a hand-written prompt** on a measurable metric
5. Take-homes: repo AND method (workflow doc)

## Theme: Crop Duster to Starship

- OLD way = crop duster: hand-tuned prompts, low altitude, exhausting, breaks on model swap
- NEW way = starship: declared signatures, composable modules, optimizer-crafted prompts, portable
- X-ray glasses = `dspy.inspect_history()` shows the actual prompt DSPy sent to the LM

**Retired**: Mission Control / Artemis theme from May. Do not use.

## The 40-minute structure

| Time | Segment | Cells | Slides |
|---|---|---|---|
| 0:00-0:03 | Opening, x-ray glasses tease | - | 1, 2 |
| 0:03-0:12 | 1st third: Signatures (declare) | 1-6 | 3, 4, 5 |
| 0:12-0:21 | 2nd third: Modules (compose) | 7-9 | 6 |
| 0:21-0:31 | 3rd third: Optimizers (tune) + **beat the hand-tuned prompt** | 10-12 | 7 |
| 0:31-0:34 | Debrief: repo, method, related tools, connection minute | - | 8 |
| 0:34-0:40 | Lightning talk ask + closing | - | 9, 10 |
| 0:40-0:50 | Q&A | - | 10 (holds) |

## The technical spine

- Anthropic API, Claude Haiku 4.5 as main model, Sonnet 4.6 for A/B
- DSPy 3.2.x
- Single Jupyter notebook, 30+ cells, walked through live
- **LIVE**: BootstrapFewShot in under 90 seconds on stage
- **PRE-COMPILED (Sunday-ish before the talk)**: MIPROv2 artifact loaded from disk in a cell
- **NEW for this version**: A hand-written prompt baseline that DSPy beats on a metric. This IS the "beat a hand-written prompt" moment.

## What exists (as of Jul 15 2026)

**In Claude artifacts from prior sessions** (accessible from your Claude account):
- Old notebook (28 cells, Mission Control themed)
- Old slide deck (10 slides, Mission Control themed)
- Old CLAUDE.md, TIMELINE.md, SPEAKER_NOTES.md (all Mission Control themed)
- Old setup.py, run_miprov2.py, execute_notebook.py (theme-agnostic, still valid)

**In this project (`/mnt/project/`)**:
- 3 planning docs from May: high-level plan, materials list, 5-hour MVP plan

**In your GitHub**: whatever you pushed. Probably nothing. If you did push, the repo is `dspy_mission_control` under your personal account.

**On your laptop**: possibly nothing survived. Assume rebuilding.

## What is being rebuilt tonight in this session

- `CATCHUP.md` (this file)
- `CLAUDE.md` (Claude Code instructions, retimed to 40+10)
- `TIMELINE.md` (40-min structure with the new demo)
- `SPEAKER_NOTES.md` (Crop Duster to Starship language)
- `dspy_starship.ipynb` (renamed and retimed notebook)
- `scripts/setup.py`, `scripts/run_miprov2.py`, `scripts/execute_notebook.py` (theme-agnostic, mostly unchanged)
- `requirements.txt`, `.env.example`, `.gitignore`
- Bootstrap prompt for Claude Code Desktop

Slide deck reskin is separate work. Old deck (Mission Control) still usable if you swap the text. Better plan: rebuild deck cleanly, but that is second priority tonight.

## What you need to do tonight

1. Download the zip Claude produces at the end of this session
2. Unzip into a working directory on your laptop
3. Open Claude Code Desktop, point it at that directory
4. Paste the bootstrap prompt
5. Let Claude Code run setup.py
6. Paste your Anthropic API key into `.env`
7. Let Claude Code run the notebook end-to-end to verify it works
8. Stop for tonight

Everything else waits.

## What Claude Code MUST NOT do

- Shorten the talk (it is 40 min + 10 Q&A, not 15, not 30)
- Remove MIPROv2
- Remove BootstrapFewShot
- Remove the beat-the-hand-tuned-prompt demo
- Change the Crop Duster to Starship theme
- Push to GitHub without asking
- Rewrite files it was not asked to rewrite

## The single most important sentence

**"Build the whole thing live, beat a hand-written prompt, and send you home with a repo and a method."**

That is the promise in the meetup description. Every prep decision serves that sentence.
