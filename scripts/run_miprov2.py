"""
run_miprov2.py

Compiles the sophisticated optimizer artifact for the talk. Run this BEFORE
the talk (Sunday-equivalent prep). Tries MIPROv2 first. If MIPROv2 errors
(for example, the optional 'optuna' dependency is missing), falls back to
BootstrapFewShotWithRandomSearch.

Either way, produces miprov2_artifact.json at the repo root. The MIPROv2 half
of cell 12 in the notebook loads this file during the live talk.

On the confirmed-vs-suspected task with Haiku 4.5 as the task model and Sonnet
4.6 as the instruction proposer, the heavy MIPROv2 run scores 100% on the
held-out test set and writes the labeling convention out as an instruction.

Usage:
    python scripts/run_miprov2.py

Wall-clock is roughly 5 to 10 minutes on the settings below. Measured cost is
under $1. Let it run in the background while you do other prep.
"""
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"
ARTIFACT = REPO_ROOT / "miprov2_artifact.json"


def build_data(dspy):
    """Return (trainset, valset). Convention: confirmed threat = urgent;
    suspected / unconfirmed / in-tolerance = attention; normal, drill, test,
    or completed = routine."""
    def ex(t, u):
        return dspy.Example(transmission=t, urgency=u).with_inputs("transmission")

    train = [
        ex("Confirmed cabin depressurization, crew on emergency oxygen.", "urgent"),
        ex("Main bus B undervolt confirmed, switching to backup now.", "urgent"),
        ex("Confirmed hull breach in module three, sealing bulkheads now.", "urgent"),
        ex("Fire confirmed in the galley, suppression activated, crew evacuating.", "urgent"),
        ex("Confirmed ammonia leak in the cooling loop, crew donning masks.", "urgent"),
        ex("Reactor temperature confirmed past the red line, emergency shutdown started.", "urgent"),
        ex("Confirmed loss of main power, running on reserve batteries now.", "urgent"),
        ex("Collision confirmed, debris impact in ninety seconds, brace.", "urgent"),
        ex("Confirmed oxygen leak, cabin pressure falling now, masks on.", "urgent"),
        ex("Engine overpressure confirmed, shutting down the affected thruster.", "urgent"),
        ex("Confirmed toxic fumes in the crew cabin, evacuating to the safe module.", "urgent"),
        ex("Water intrusion confirmed in the avionics bay, powering down affected units.", "urgent"),
        ex("Confirmed runaway heater, temperature climbing fast, cutting power now.", "urgent"),
        ex("Structural crack confirmed spreading on the truss, crew to the safe zone.", "urgent"),
        ex("Suspected coolant leak, still confirming whether it is real.", "attention"),
        ex("Unidentified vibration of unknown origin, investigating.", "attention"),
        ex("Possible sensor fault causing erratic temperature readings, assessing.", "attention"),
        ex("Intermittent alarm with no confirmed cause, monitoring.", "attention"),
        ex("Fuel pressure trending low but still within limits, watching.", "attention"),
        ex("Faint odor reported near the galley, source not yet identified.", "attention"),
        ex("One sensor shows a pressure dip; others read normal, checking.", "attention"),
        ex("Slight orbital drift detected, cause under review, still nominal.", "attention"),
        ex("Possible micro-leak suspected in a fuel line, not yet verified.", "attention"),
        ex("Unusual telemetry pattern, cause unclear, gathering more data.", "attention"),
        ex("Battery temperature slightly elevated but within spec, monitoring.", "attention"),
        ex("Unconfirmed radiation blip on one detector, cross-checking others.", "attention"),
        ex("Comms static increasing, cause not yet determined, investigating.", "attention"),
        ex("Scheduled fire drill completed, all crew accounted for.", "routine"),
        ex("Morning status check, all systems nominal.", "routine"),
        ex("Radiation monitor calibration finished, readings as expected.", "routine"),
        ex("Evening meal service proceeding on schedule.", "routine"),
        ex("Airlock leak-check test passed within nominal limits.", "routine"),
        ex("Daily science experiment completed on schedule.", "routine"),
        ex("Routine comms handover to the next ground station complete.", "routine"),
        ex("Scheduled solar panel cleaning cycle finished normally.", "routine"),
        ex("Weekly emergency equipment inspection completed, all nominal.", "routine"),
        ex("Planned software update installed successfully, systems nominal.", "routine"),
        ex("Crew sleep shift change logged, all normal.", "routine"),
        ex("Scheduled thruster test fired nominally, within parameters.", "routine"),
        ex("Routine water quality sample taken, results normal.", "routine"),
    ]

    val = [
        ex("Confirmed fuel line rupture, venting propellant, isolating now.", "urgent"),
        ex("Depressurization confirmed in the lab module, hatch sealed.", "urgent"),
        ex("Confirmed electrical fire on panel four, extinguishing now.", "urgent"),
        ex("Life support failure confirmed, backup scrubber online now.", "urgent"),
        ex("Confirmed coolant loss, reactor temperature rising, acting now.", "urgent"),
        ex("Cabin smoke confirmed thickening, crew moving to the safe haven.", "urgent"),
        ex("Confirmed thruster stuck open, attitude diverging, correcting now.", "urgent"),
        ex("Possible coolant odor near bay two, source unconfirmed, checking.", "attention"),
        ex("Unverified pressure spike on one gauge, others nominal, watching.", "attention"),
        ex("Slight antenna misalignment within tolerance, monitoring.", "attention"),
        ex("Unexplained noise from the aft module, investigating the cause.", "attention"),
        ex("Suspected loose connector causing a flicker, not yet confirmed.", "attention"),
        ex("Minor attitude wobble within limits, keeping an eye on it.", "attention"),
        ex("Possible software glitch reported, cannot reproduce it yet.", "attention"),
        ex("Scheduled emergency drill completed, all stations reported ready.", "routine"),
        ex("Water recycling system test passed as expected.", "routine"),
        ex("Midday systems check nominal across all subsystems.", "routine"),
        ex("Crew exercise session logged and complete.", "routine"),
        ex("Planned antenna repointing completed on schedule.", "routine"),
        ex("Routine cargo transfer finished without issues.", "routine"),
    ]
    return train, val


def main():
    load_dotenv(ENV_FILE)
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in .env")
        return 1

    import dspy

    task_model = dspy.LM("anthropic/claude-haiku-4-5-20251001", max_tokens=800, temperature=0.0)
    proposer_model = dspy.LM("anthropic/claude-sonnet-4-6", max_tokens=2000, temperature=1.0)
    dspy.configure(lm=task_model)

    class ClassifyTransmission(dspy.Signature):
        """Classify a spacecraft transmission by urgency."""
        transmission: str = dspy.InputField()
        urgency: str = dspy.OutputField(desc="One of: routine, attention, urgent")

    train, val = build_data(dspy)

    def match(example, pred, trace=None):
        return example.urgency.strip().lower() == pred.urgency.strip().lower()

    print(f"Compiling optimizer artifact at {ARTIFACT}")
    print(f"Started at {time.strftime('%H:%M:%S')}")
    print()

    artifact = None
    optimizer_used = None

    try:
        from dspy.teleprompt import MIPROv2
        print("Attempting MIPROv2 heavy (roughly 5 to 10 minutes)...")
        miprov2 = MIPROv2(
            metric=match,
            prompt_model=proposer_model,
            task_model=task_model,
            auto="heavy",
            max_bootstrapped_demos=4,
            max_labeled_demos=16,
            num_threads=8,
            seed=9,
        )
        artifact = miprov2.compile(
            student=dspy.Predict(ClassifyTransmission),
            trainset=train,
            valset=val,
            view_data_batch_size=15,
            requires_permission_to_run=False,
        )
        optimizer_used = "MIPROv2"
        print("MIPROv2 succeeded.")
    except Exception as e:
        print(f"MIPROv2 errored: {e}")
        print()
        print("Falling back to BootstrapFewShotWithRandomSearch (5 to 10 minutes)...")
        print("If the error mentions 'optuna', install it: pip install optuna")
        from dspy.teleprompt import BootstrapFewShotWithRandomSearch
        bsrs = BootstrapFewShotWithRandomSearch(
            metric=match,
            max_bootstrapped_demos=4,
            max_labeled_demos=16,
            num_candidate_programs=6,
        )
        artifact = bsrs.compile(
            student=dspy.Predict(ClassifyTransmission),
            trainset=train,
        )
        optimizer_used = "BootstrapFewShotWithRandomSearch"

    artifact.save(str(ARTIFACT))
    size_kb = ARTIFACT.stat().st_size / 1024
    try:
        instruction = artifact.signature.instructions
    except Exception:
        instruction = "(unavailable)"
    print()
    print(f"Saved: {ARTIFACT} ({size_kb:.1f} KB)")
    print(f"Optimizer used: {optimizer_used}")
    print(f"Instruction it wrote:\n  {instruction}")
    print(f"Finished at {time.strftime('%H:%M:%S')}")
    print()
    print("The MIPROv2 half of cell 12 will load this file during the talk.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
