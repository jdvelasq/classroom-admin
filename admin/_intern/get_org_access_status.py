from admin._intern.get_org_repos import get_org_repos
from admin._intern.gh import run_gh_json


def get_org_access_status(org_name):

    repo_names = get_org_repos(org_name)
    status = {}

    print("\n\nObtaining access status for each repository...\n\n")

    for repo_name in repo_names:

        print(f"  {repo_name}...", flush=True)

        collaborators = run_gh_json(
            [
                "api",
                f"/repos/{org_name}/{repo_name}/collaborators?affiliation=direct",
            ]
        )

        if collaborators:
            student = collaborators[0]["login"]
            status[repo_name] = {"status": "accepted", "student": student}
            continue

        invitations = run_gh_json(["api", f"/repos/{org_name}/{repo_name}/invitations"])

        if not invitations:
            status[repo_name] = {"status": "not_invited", "student": None}
        else:
            invitation = invitations[0]
            student = invitation["invitee"]["login"]
            invitation_status = "expired" if invitation["expired"] else "pending"
            status[repo_name] = {"status": invitation_status, "student": student}

    print("\n")

    return status
