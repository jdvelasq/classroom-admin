"""Create the students.txt from roster."""

import pandas as pd

# Data:

path = "data/descriptiva"

roster = pd.read_csv(f"{path}/classroom_roster.csv")
usernames = roster.github_username.tolist()
usernames = [u for u in usernames if isinstance(u, str) and len(u) > 0]


with open(f"{path}/students.txt", "w") as f:
    for u in usernames:
        f.write(f"{u}\n")