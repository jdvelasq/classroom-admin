"""Create the student repo if not exists."""

import subprocess
import time

# Data:
org = "2025-2-descriptiva"
path = "data/descriptiva"

# Read data from files
with open(f"{path}/students.txt") as f:
    students = [line.strip() for line in f.readlines()]

with open(f"{path}/templates.txt") as f:
    templates = [line.strip() for line in f.readlines() if line.strip()]

with open(f"{path}/prefixes.txt") as f:
    prefixes = [line.strip() for line in f.readlines() if line.strip()]

fail = False
counter = 10

for i_student, student in enumerate(students):

    if student == "":
        break

    print(f"[{i_student+1}/{len(students)}] Processing student: {student}")

    for template, prefix in zip(templates, prefixes):
        
        repo_name = f"{prefix}-{student}"

        result = subprocess.run(["./create.sh", org, repo_name, template])

        counter -= 1

        if counter > 0:
            time.sleep(3)
        else:
            counter = 10
            print()
            print("  Pausing for avoiding rate limit")
            print()
            time.sleep(30)

        if result.returncode != 0:
            fail = True
            break

    if fail:
        print("  Exiting!")
        exit()

    
    # print()
    # print("Waiting 90 seconds to avoid rate limiting...")
    # print()
    # time.sleep(90)

print("finished!")