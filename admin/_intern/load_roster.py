import pandas as pd


def load_roster():

    roster_path = "roster.csv"
    roster = pd.read_csv(
        roster_path, header=None, names=["nombre", "email", "username"]
    )

    roster["email"] = roster["email"].str.lower()

    roster["username"] = roster["username"].str.lower()

    return roster
