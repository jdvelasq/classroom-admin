from admin._intern import (
    get_org_access_status,
    get_repo_to_username,
    invite_collaborator,
)
from admin._intern.gh import GhError


def grant_access(org_name):

    repo_to_username = get_repo_to_username()
    status = get_org_access_status(org_name)
    status = {
        k: v for k, v in status.items() if v["status"] not in ["accepted", "pending"]
    }

    n_missing_access = len(status)

    if n_missing_access == 0:
        print(f"\n\nAll roster repos have access in {org_name}.\n\n")
        return
    else:
        print(f"\n\n{n_missing_access} repos without access in {org_name}:\n")

    for repo_name, info in status.items():

        if repo_name not in repo_to_username:
            print()
            print(f"     {repo_name} -> (no student on file)")
            print()
            continue

        username = repo_to_username[repo_name]

        if not username:
            print(f"  {repo_name} -> (no GitHub username on file)")
            continue

        print(f"  {repo_name} -> {username} ({info['status']}, sending invitation)")

        try:
            invite_collaborator(org_name, repo_name, username)
        except GhError as error:
            print(f"    ! failed to invite {username} to {repo_name}: {error}")

    print()
    print()
