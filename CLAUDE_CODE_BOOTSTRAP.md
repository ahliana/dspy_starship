# Claude Code Bootstrap Prompt

**Paste this VERBATIM as your first message to Claude Code Desktop after opening the `dspy_starship` folder.**

---

I am preparing a 40-minute talk on DSPy for PyHou. The talk is Tuesday July 21, 2026 at 6:40 PM. Q&A runs 7:20 to 7:30 PM. Total 50 minutes with Q&A.

**Before you do anything, read these files in this exact order:**

1. `CATCHUP.md` (my summary of the project)
2. `CLAUDE.md` (master instructions, READ COMPLETELY)
3. `TIMELINE.md` (the LOCKED 40+10 structure)
4. `SPEAKER_NOTES.md` (what I will say)
5. `README.md` (file map)

Do not read anything else yet. Do not run anything yet. Do not "improve" anything.

**This is a 40-minute talk plus 10-minute Q&A. Not 15. Not 30. FORTY MINUTES.**

A previous Claude Code session shortened my talk to 15 minutes and removed MIPROv2 and the beat-the-hand-tuned-prompt demo. This wasted my Sunday. I am short on time. Do not do that. If you are tempted to "simplify" or "shorten" anything, STOP and ASK.

**The submitted talk description promises FIVE specific things. Every one MUST ship:**

1. Declare + compose + optimize (three DSPy primitives, in order)
2. X-ray glasses (`dspy.inspect_history()` as running metaphor)
3. Build the whole thing LIVE on stage
4. **Beat a hand-written prompt on a measurable metric** (this is cell 11 and 12 of the notebook)
5. Take home a repo AND a method (`METHOD.md`)

If you drop any of the five, I have failed my audience.

**After you finish reading the 5 files, respond with EXACTLY this:**

> "I read CATCHUP.md, CLAUDE.md, TIMELINE.md, SPEAKER_NOTES.md, and README.md. The talk is 40 minutes plus 10 minutes Q&A. The theme is Crop Duster to Starship. The five description promises are declare-compose-optimize, x-ray glasses via inspect_history, build-live-on-stage, beat-a-hand-written-prompt, and repo-plus-method. I will not shorten, simplify, or remove anything without your explicit permission. Ready for Task 1: environment setup. Should I run `python scripts/setup.py`?"

Then wait for my "yes" before running anything.
