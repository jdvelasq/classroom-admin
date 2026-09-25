import pandas as pd

from admin._intern import load_google, load_roster, save_roster


def update_usernames_from_google():

    roster = load_roster()
    google = load_google()

    print(f"\n\nFound {roster['username'].isna().sum()} missing usename in roster.csv.")
    print(f"Found {len(google)} entries in google.tsv.")

    google["username"] = google["username"].apply(lambda x: x.split("/")[-1])

    missing = roster["username"].isna() | (
        roster["username"].astype(str).str.strip() == ""
    )

    # map avoids row duplication from merge when email is not unique in either dataframe
    email_to_username = google.drop_duplicates(subset="email", keep="first").set_index(
        "email"
    )["username"]
    roster.loc[missing, "username"] = roster.loc[missing, "email"].map(
        email_to_username
    )

    print(f"New {roster['username'].isna().sum()} missing usernames roster.csv.\n\n")

    save_roster(roster)
