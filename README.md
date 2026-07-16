# DSPy Starship

**From Crop Duster to Starship: Let DSPy Tune Your Prompts in Plain Python**

Talk delivered at PyHou on July 21, 2026. This repo is the take-home artifact.

## What is here

| File | What it is |
|---|---|
| `TIMELINE.md` | The locked 40-minute talk breakdown plus 10 min Q&A |
| `SPEAKER_NOTES.md` | What to say at each cell and slide |
| `dspy_starship_01.ipynb` | The notebook that IS the talk, walked through live. Fully annotated for self-study. Start here |
| `METHOD.md` | The workflow write-up. This is the "method" take-home |
| `slides.html` | The 10-slide deck, self-contained. Open in a browser, F11, arrow keys |
| `backups/full_demo.ipynb` | Pre-executed copy with all outputs, the offline fallback |
| `scripts/setup.py` | Environment setup, Python |
| `scripts/run_miprov2.py` | Compiles the sophisticated optimizer artifact |
| `scripts/execute_notebook.py` | Runs the notebook end-to-end, saves offline backup |
| `requirements.txt` | Pinned dependencies |
| `.env.example` | Copy to `.env`, uncomment your `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` |

## Quick start

```
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python scripts/setup.py
```

Optional, since the compiled artifact and the offline backup already ship with the repo:

```
python scripts/run_miprov2.py      # rebuild miprov2_artifact.json (5-10 min)
python scripts/execute_notebook.py # rebuild backups/full_demo.ipynb
```

Then open `dspy_starship_01.ipynb` in Jupyter. It runs on either an Anthropic or an OpenAI key: put whichever one you have in `.env` and the first cell picks the right models.

## The talk in one sentence

DSPy takes hand-tuned prompts (the crop duster) and turns them into declared programs the optimizer can tune (the starship), in plain Python. `dspy.inspect_history()` is the x-ray glasses that let you see every prompt the library sent.

## The five promises

The submitted meetup description promises five things. Every deliverable in this repo serves them:

1. Declare + compose + optimize (the three primitives)
2. X-ray glasses: `dspy.inspect_history()` as a running metaphor
3. Build the whole thing LIVE
4. Beat a hand-written prompt on a metric
5. Take home a repo AND a method

## Continue the mission

- PyHou Discord: [add link]
- LinkedIn: [add link]
- Recording on TechTalk YouTube: [link after upload]

## License

MIT. See [LICENSE](LICENSE).

Built for PyHou at Improving Houston.
