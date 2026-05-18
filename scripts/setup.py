"""
setup.py

Sets up the Python environment for the DSPy Mission Control talk.
Run this ONCE. It will:
  1. Verify Python version >= 3.10
  2. Install required packages
  3. Copy .env.example to .env if missing
  4. Run a smoke test if ANTHROPIC_API_KEY is set
  5. Print SETUP COMPLETE on success

Usage:
    python scripts/setup.py
"""
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
        contents = ENV_FILE.read_text()
        if "your-anthropic-api-key-here" in contents:
            print("WARNING: .env still contains the placeholder API key.")
            print("Edit .env and set ANTHROPIC_API_KEY=sk-ant-... before running anything else.")
            return False
        if "ANTHROPIC_API_KEY=" not in contents:
            print("WARNING: .env does not contain ANTHROPIC_API_KEY")
            return False
        print("OK: .env exists with a real key")
        return True
    if ENV_EXAMPLE.exists():
        shutil.copy(ENV_EXAMPLE, ENV_FILE)
        print("Copied .env.example to .env")
        print("WARNING: Edit .env and set ANTHROPIC_API_KEY before running anything else.")
        return False
    print(f"ERROR: Neither {ENV_FILE} nor {ENV_EXAMPLE} found")
    return False


def smoke_test():
    """Verify DSPy + Anthropic talk to each other."""
    print("Running smoke test...")
    try:
        from dotenv import load_dotenv
        load_dotenv(ENV_FILE, override=True)
        import dspy
        lm = dspy.LM("anthropic/claude-haiku-4-5-20251001", max_tokens=200)
        dspy.configure(lm=lm)
        result = dspy.Predict("question -> answer")(question="What city houses NASA Mission Control?")
        print(f"OK: smoke test answer: {result.answer[:100]}")
        return True
    except Exception as e:
        print(f"ERROR: smoke test failed: {e}")
        return False


def main():
    print("=" * 60)
    print("DSPy Mission Control: Environment Setup")
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
            print("  1. python scripts/run_miprov2.py  (Sunday prep, 30-45 min)")
            print("  2. python scripts/execute_notebook.py  (offline backup)")
            return 0
    print()
    print("Setup incomplete. Fix the issues above and re-run.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
