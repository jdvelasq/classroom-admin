"""Add the outsider collaborator (permission) to the student repo"""

import subprocess

# Data:
org = "2025-2-descriptiva"
path = "data/descriptiva"

# Read data from files
with open(f"{path}/students.txt") as f:
    students = [line.strip() for line in f.readlines() if line.strip()]

with open(f"{path}/templates.txt") as f:
    templates = [line.strip() for line in f.readlines() if line.strip()]

with open(f"{path}/prefixes.txt") as f:
    prefixes = [line.strip() for line in f.readlines() if line.strip()]


for i_student, student in enumerate(students):

    if student == "":
        break

    print(f"[{i_student+1}/{len(students)}] Processing student: {student}")

    for template, prefix in zip(templates, prefixes):
        repo_name = f"{prefix}-{student}"
        
        subprocess.run(
            [
                "./access.sh", 
                org, 
                repo_name, 
                student
                ]
            )
