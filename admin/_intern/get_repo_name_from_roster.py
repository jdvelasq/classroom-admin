from admin._intern.load_roster import load_roster


def get_repo_name_from_roster():

    roster = load_roster()
    repos = roster["nombre"]
    repos = repos.str.replace(" ", "-", regex=False)
    repos = repos.tolist()
    repos = ["std-" + repo for repo in repos]

    return repos
