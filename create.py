"""Create the student repo if not exists."""

import subprocess
import time

# Data:
org = "2025-2-predictiva"
path = "data/predictiva"

# Read data from files
with open(f"{path}/students.txt") as f:
    students = [line.strip() for line in f.readlines() if line.strip()]

with open(f"{path}/templates.txt") as f:
    templates = [line.strip() for line in f.readlines() if line.strip()]

with open(f"{path}/prefixes.txt") as f:
    prefixes = [line.strip() for line in f.readlines() if line.strip()]

fail = False
for i_student, student in enumerate(students):

    print(f"[{i_student+1}/{len(students)}] Processing student: {student}")
    
    for template, prefix in zip(templates, prefixes):
        
        repo_name = f"{prefix}-{student}"

        max_retries = 3

        for attempt in range(max_retries):
            result = subprocess.run(["./create.sh", org, repo_name, template])
            if result.returncode == 0:
                time.sleep(5) 
                break
            else:
                if attempt < max_retries - 1:
                    time.sleep(20)
                else:
                    print(f"  All attempts failed.")
                    fail = True
                    break

        if fail:
            break

    if fail:
        print("  Exiting!")
        exit()

    
    print()
    print("Waiting 60 seconds to avoid rate limiting...")
    print()
    time.sleep(60)