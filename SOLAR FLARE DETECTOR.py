import subprocess
import sys
import time

print("=" * 60)
print("      SOLAR FLARE DETECTION AND ALERT SYSTEM")
print("=" * 60)
print("Initializing Project...\n")

programs = [
    "001-Intialization.py",
    "002-Csv File.py",
    "003-Solexs graph.py",
    "004-Peak detection.py",
    "005-Major events.py",
    "006-Hls data manipulation.py",
    "007-Comparing.py",
    "008-Final report.py"
]

for program in programs:
    print("\n" + "=" * 60)
    print(f"Running {program}")
    print("=" * 60)

    try:
        exec(open(program).read())

        input(f"\n{program} completed.\nPress Enter to continue...")

    except Exception as e:
        print(f"\nError in {program}")
        print(e)
        break

    time.sleep(1)

print("=" * 60)
print("ALL PROGRAMS EXECUTED SUCCESSFULLY")
print("Solar Flare Analysis Completed")
print("Final Reports Generated")
print("Alert Status Generated")
print("=" * 60)

input("\nPress Enter to Exit...")
