import time

from admin._intern import create_repo, get_org_repos, get_roster_repos


def create(org_name):

    roster_repos = get_roster_repos()
    org_repos = get_org_repos(org_name)
    missing_repos = [repo for repo in roster_repos if repo not in org_repos]

    n_missing_repos = len(missing_repos)

    if n_missing_repos == 0:
        print(f"\n\nAll roster repos already exist in {org_name}.\n\n")
        return
    else:
        print(f"\n\n{n_missing_repos} missing repos in {org_name}:\n")

    time.sleep(1)
    for index, repo_name in enumerate(missing_repos):
        print(f"  {1+index:03d} of {n_missing_repos}: {org_name}/{repo_name}")
        create_repo(org_name, repo_name)
        time.sleep(1)

    print()
