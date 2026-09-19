import pandas as pd


def load_google():

    google_path = "google.tsv"

    google = pd.read_csv(
        google_path, header=None, names=["email", "username"], sep="\t"
    )

    google["email"] = google["email"].str.lower()
    google["email"] = google["email"].str.strip()
    google["email"] = google["email"].apply(
        lambda x: x if "@" in x else f"{x}@unal.edu.co"
    )

    google["username"] = google["username"].str.lower()
    google["username"] = google["username"].str.strip()
    google["username"] = google["username"].apply(
        lambda x: (
            x if x.startswith("https://github.com/") else f"https://github.com/{x}"
        )
    )

    google = google.drop_duplicates(subset=["email"], keep="first")

    return google
