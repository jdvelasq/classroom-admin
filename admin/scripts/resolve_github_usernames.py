import time

import pandas as pd

from admin._intern import get_username_from_email, load_roster
from admin._intern.save_roster import save_roster


def resolve_github_usernames(org_name):

    roster = load_roster()

    n_missing = (roster["username"] == "" | pd.isna(roster["username"])).sum()

    print(f"\n\nFound {n_missing} missing usernames in roster.\n\n")

    for index, row in roster.iterrows():

        if row["username"] == "" or pd.isna(row["username"]):

            print(f"Resolving username for {row['nombre']} ({row['email']})...")
            username = get_username_from_email(row["email"])
            roster.loc[index, "username"] = username or ""

            save_roster(roster)

            time.sleep(2)

    print("\n")
