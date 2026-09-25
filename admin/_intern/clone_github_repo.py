from admin._intern.gh import run_gh


def clone_github_repo(org_name, repo_name):

    run_gh(
        [
            "repo",
            "clone",
            f"{org_name}/{repo_name}",
            f"../repos/{repo_name}",
            "--",
            "--depth",
            "1",
        ]
    )
