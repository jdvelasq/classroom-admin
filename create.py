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


counter = 10

for i_student, student in enumerate(students):

    if student == "":
        break

    print(f"[{i_student+1}/{len(students)}] Processing student: {student}")

    for template, prefix in zip(templates, prefixes):
        
        repo_name = f"{prefix}-{student}"

        while True:

            result = subprocess.run(["./create.sh", org, repo_name, template])

            if result.returncode == 0:

                counter -= 1
                retries = 0

                if counter > 0:
                    time.sleep(3)
                else:
                    counter = 10
                    print("\n  Pausing for avoiding rate limit\n")
                    time.sleep(45)

                break
            
            counter = 10
            retries += 1
            time_to_sleep = 1
            if retries <= 5:
                time_to_sleep = 5 
            print(f"           ({retries:>2d}) Retrying in {time_to_sleep} minutes", end="", flush=True)
            for _ in range(time_to_sleep * 6):                
                time.sleep(10)
                print(".", end="", flush=True)
            print()


print("finished!")