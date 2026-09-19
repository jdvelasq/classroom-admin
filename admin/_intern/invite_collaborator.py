from admin._intern.gh import run_gh


def invite_collaborator(org_name, repo_name, username, permission="push"):

    run_gh(
        [
            "api",
            "--method",
            "PUT",
            f"/repos/{org_name}/{repo_name}/collaborators/{username}",
            "-f",
            f"permission={permission}",
        ]
    )
