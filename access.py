"""Add the outsider collaborator (permission) to the student repo"""

import subprocess

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


for student in students:
    print(f"Processing student: {student}")
    for template, prefix in zip(templates, prefixes):
        repo_name = f"{prefix}-{student}"
        subprocess.run(
            [
                "./access.sh", 
                org, 
                repo_name, 
                student,
                ]
            )
