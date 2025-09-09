"""Extracts e-mails from calendar"""

import pandas as pd

path = "data/descriptiva"

df = pd.read_csv(f"{path}/emails.txt", header=None, names=["name"])

# captures all text between < and >
df["email"] = df["name"].str.extract(r'<(.*?)>')


for email in df["email"]:
    print(email)