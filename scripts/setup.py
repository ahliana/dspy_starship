"""
setup.py

Sets up the Python environment for the DSPy Starship talk.

Run this ONCE. It will:
  1. Verify Python version >= 3.10
  2. Install required packages
  3. Copy .env.example to .env if missing
  4. Run a smoke test if ANTHROPIC_API_KEY is set
  5. Print SETUP COMPLETE on success

Usage:
    python scripts/setup.py
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MIN_PY = (3, 10)
REQUIREMENTS = REPO_ROOT / "requirements.txt"
ENV_FILE = REPO_ROOT / ".env"
ENV_EXAMPLE = REPO_ROOT / ".env.example"


def check_python_version():
    if sys.version_info < MIN_PY:
        print(f"ERROR: Python {MIN_PY[0]}.{MIN_PY[1]}+ required. Found {sys.version}")
        sys.exit(1)
    print(f"OK: Python {sys.version_info.major}.{sys.version_info.minor}")


def install_requirements():
    if not REQUIREMENTS.exists():
        print(f"ERROR: {REQUIREMENTS} not found")
        sys.exit(1)
    print(f"Installing {REQUIREMENTS}...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS), "--quiet"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("ERROR: pip install failed")
        print(result.stderr)
        sys.exit(1)
    print("OK: dependencies installed")


def ensure_env_file():
    if ENV_FILE.exists():
        keys = {}
        for line in ENV_FILE.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                name, _, value = line.partition("=")
                keys[name.strip()] = value.strip()
        real = [k for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY")
                if keys.get(k) and not keys[k].startswith("your-")]
        if real:
            print(f"OK: .env has a real key ({', '.join(real)})")
            return True
        print("WARNING: .env has no real key yet.")
        print("Edit .env and set ANTHROPIC_API_KEY or OPENAI_API_KEY.")
        return False
    if ENV_EXAMPLE.exists():
        shutil.copy(ENV_EXAMPLE, ENV_FILE)
        print("Copied .env.example to .env")
        print("WARNING: Edit .env and set ANTHROPIC_API_KEY or OPENAI_API_KEY before running anything else.")
        return False
    print(f"ERROR: Neither {ENV_FILE} nor {ENV_EXAMPLE} found")
    return False


def smoke_test():
    """Verify DSPy talks to whichever provider has a key."""
    print("Running smoke test...")
    try:
        from dotenv import load_dotenv
        load_dotenv(ENV_FILE)
        import dspy
        anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
        if anthropic_key and not anthropic_key.startswith("your-"):
            model = "anthropic/claude-haiku-4-5-20251001"
        else:
            model = "openai/gpt-4o-mini"
        lm = dspy.LM(model, max_tokens=200)
        dspy.configure(lm=lm)
        result = dspy.Predict("question -> answer")(question="What year was DSPy released?")
        print(f"OK: smoke test ({model}) answer: {result.answer[:100]}")
        return True
    except Exception as e:
        print(f"ERROR: smoke test failed: {e}")
        return False


def main():
    print("=" * 60)
    print("DSPy Starship: Environment Setup")
    print("=" * 60)
    check_python_version()
    install_requirements()
    env_ready = ensure_env_file()
    if env_ready:
        if smoke_test():
            print()
            print("=" * 60)
            print("SETUP COMPLETE")
            print("=" * 60)
            print()
            print("Next steps:")
            print("  1. Open dspy_starship_01.ipynb in Jupyter and run it top to bottom")
            print("  2. Optional: python scripts/run_miprov2.py  (5-10 min; a compiled artifact already ships with the repo)")
            print("  3. Optional: python scripts/execute_notebook.py  (rebuild the offline backup)")
            return 0
    print()
    print("Setup incomplete. Fix the issues above and re-run.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
