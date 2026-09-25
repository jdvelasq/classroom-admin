def get_repo_name_to_username():

    repo_to_username = {}

    with open("roster.csv") as f:

        for line in f:

            name, _, username = line.strip().split(",")
            repo_name = "std-" + name.replace(" ", "-")

            repo_to_username[repo_name] = username

    return repo_to_username
