"""
run_miprov2.py

Sunday prep. Compiles a sophisticated optimizer artifact for the talk.
Tries MIPROv2 first (30-45 min). If MIPROv2 errors, falls back to
BootstrapFewShotWithRandomSearch (5-10 min).

Either way, produces miprov2_artifact.json at the repo root.
Cell 11 of the notebook loads this file during the live talk.

Usage:
    python scripts/run_miprov2.py

This is a long-running script. Let it run in the background while you do
other prep. Approximate cost on Haiku 4.5: $1 to $3.
"""
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"
ARTIFACT = REPO_ROOT / "miprov2_artifact.json"


def main():
    load_dotenv(ENV_FILE, override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in .env")
        return 1

    import dspy

    lm = dspy.LM("anthropic/claude-haiku-4-5-20251001", max_tokens=800)
    dspy.configure(lm=lm)

    # Match the signature and training data from notebook cell 10
    class ClassifyTransmission(dspy.Signature):
        """Classify a mission transmission by urgency."""
        transmission: str = dspy.InputField()
        urgency: str = dspy.OutputField(desc="One of: routine, attention, urgent")

    train = [
        # Clear-cut cases
        dspy.Example(transmission="Routine status check, all systems nominal.",
                     urgency="routine").with_inputs("transmission"),
        dspy.Example(transmission="Minor cabin pressure fluctuation detected.",
                     urgency="attention").with_inputs("transmission"),
        dspy.Example(transmission="Main bus B undervolt, immediate response required.",
                     urgency="urgent").with_inputs("transmission"),
        dspy.Example(transmission="Daily science experiment completed on schedule.",
                     urgency="routine").with_inputs("transmission"),
        dspy.Example(transmission="Slight trajectory deviation, investigating cause.",
                     urgency="attention").with_inputs("transmission"),
        dspy.Example(transmission="Cabin fire detected, crew evacuating to lifeboat.",
                     urgency="urgent").with_inputs("transmission"),
        # Ambiguous cases without obvious urgency words
        dspy.Example(transmission="Solar array pointing error 0.3 degrees, automatic correction failed twice.",
                     urgency="attention").with_inputs("transmission"),
        dspy.Example(transmission="Crew morale low after fourth straight day of docking delays.",
                     urgency="attention").with_inputs("transmission"),
        dspy.Example(transmission="Coolant loop B isolation valve will not close, loop A still nominal.",
                     urgency="urgent").with_inputs("transmission"),
        dspy.Example(transmission="Hydroponics shelf 4 humidity 92 percent, dehumidifier running but not catching up.",
                     urgency="attention").with_inputs("transmission"),
        dspy.Example(transmission="Cabin air filter scheduled replacement complete, performance nominal.",
                     urgency="routine").with_inputs("transmission"),
        dspy.Example(transmission="Robotic arm joint 3 actuator drawing 15 percent above baseline current.",
                     urgency="attention").with_inputs("transmission"),
    ]

    def match(example, pred, trace=None):
        return example.urgency.strip().lower() == pred.urgency.strip().lower()

    print(f"Compiling optimizer artifact at {ARTIFACT}")
    print(f"Started at {time.strftime('%H:%M:%S')}")
    print()

    artifact = None
    optimizer_used = None

    try:
        from dspy.teleprompt import MIPROv2
        print("Attempting MIPROv2 with auto='heavy' (this takes 30 to 45 minutes)...")
        miprov2 = MIPROv2(metric=match, auto="heavy", num_threads=4)
        artifact = miprov2.compile(
            student=dspy.Predict(ClassifyTransmission),
            trainset=train,
        )
        optimizer_used = "MIPROv2"
        print("MIPROv2 succeeded.")
    except Exception as e:
        print(f"MIPROv2 errored: {e}")
        print()
        print("Falling back to BootstrapFewShotWithRandomSearch (5 to 10 minutes)...")
        from dspy.teleprompt import BootstrapFewShotWithRandomSearch
        bsrs = BootstrapFewShotWithRandomSearch(
            metric=match,
            max_bootstrapped_demos=4,
            num_candidate_programs=6,
        )
        artifact = bsrs.compile(
            student=dspy.Predict(ClassifyTransmission),
            trainset=train,
        )
        optimizer_used = "BootstrapFewShotWithRandomSearch"

    artifact.save(str(ARTIFACT))
    size_kb = ARTIFACT.stat().st_size / 1024
    print()
    print(f"Saved: {ARTIFACT} ({size_kb:.1f} KB)")
    print(f"Optimizer used: {optimizer_used}")
    print(f"Finished at {time.strftime('%H:%M:%S')}")
    print()
    print("Verify the artifact loads correctly with:")
    print("  python -c \"import dspy; p = dspy.Predict('transmission -> urgency'); p.load('miprov2_artifact.json'); print('OK')\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
