from admin._intern.gh import run_gh


def create_repo(org_name, repo_name, template_repo="classroom-template"):

    run_gh(
        [
            "repo",
            "create",
            f"{org_name}/{repo_name}",
            "--public",
            "--template",
            f"{org_name}/{template_repo}",
        ]
    )
