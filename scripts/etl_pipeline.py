"""
ETL Pipeline for Bluestock Mutual Fund Analytics

Runs:
1. Data Cleaning
2. Data Processing
3. SQLite Loading

Author: Anil Velma
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

scripts = [
    "clean_nav_history.py",
    "clean_transactions.py",
    "clean_performance.py",
    "clean_remaining_datasets.py",
    "load_to_sqlite.py"
]

print("=" * 60)
print("Starting Bluestock Mutual Fund ETL Pipeline")
print("=" * 60)

for script in scripts:
    print(f"\nRunning: {script}")

    result = subprocess.run(
        [sys.executable, script],
        cwd=BASE_DIR,   # IMPORTANT
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"SUCCESS: {script}")
    else:
        print(f"FAILED: {script}")
        print(result.stderr)
        sys.exit(1)