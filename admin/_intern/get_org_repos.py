from admin._intern.gh import run_gh_json


def get_org_repos(org_name):

    repos = run_gh_json(["repo", "list", org_name, "--limit", "1000", "--json", "name"])
    repo_names = [repo["name"] for repo in repos]
    repo_names = [
        repo
        for repo in repo_names
        if repo not in ["classroom-data", "classroom-template", "classroom-solutions"]
    ]

    return repo_names
