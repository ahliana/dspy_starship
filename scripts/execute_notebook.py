"""
execute_notebook.py

Runs every cell in dspy_starship_01.ipynb (the notebook the talk is presented
from) end to end and saves a copy with all outputs preserved to
backups/full_demo.ipynb.

This is the offline backup if the live demo fails on stage. If wifi or the
Anthropic API is down, open backups/full_demo.ipynb in Jupyter and walk
through the pre-executed cells as if they were running live.

Usage:
    python scripts/execute_notebook.py

Approximate runtime: 5 to 10 minutes. Approximate cost on Haiku 4.5: under $1.
"""
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = REPO_ROOT / "dspy_starship_01.ipynb"
BACKUP_DIR = REPO_ROOT / "backups"
BACKUP_NOTEBOOK = BACKUP_DIR / "full_demo.ipynb"


def main():
    if not NOTEBOOK.exists():
        print(f"ERROR: {NOTEBOOK} not found")
        return 1

    BACKUP_DIR.mkdir(exist_ok=True)

    print(f"Reading {NOTEBOOK}")
    nb = nbformat.read(NOTEBOOK, as_version=4)
    print(f"  {len(nb.cells)} cells")

    print()
    print("Executing notebook end-to-end. This takes 5 to 10 minutes.")
    print()
    client = NotebookClient(
        nb,
        timeout=300,
        kernel_name="python3",
        allow_errors=False,
    )

    try:
        client.execute(cwd=str(REPO_ROOT))
    except Exception as e:
        print(f"WARNING: notebook execution had an error: {e}")
        print("The backup notebook will still be saved. Check cell-by-cell.")

    nbformat.write(nb, BACKUP_NOTEBOOK)
    size_kb = BACKUP_NOTEBOOK.stat().st_size / 1024
    print()
    print(f"Saved: {BACKUP_NOTEBOOK} ({size_kb:.1f} KB)")
    print()
    print("Offline backup ready. If live demo fails on stage:")
    print(f"  1. Open {BACKUP_NOTEBOOK} in Jupyter")
    print("  2. Walk through the pre-executed cells")
    print("  3. Audience cannot tell the difference if you narrate cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
