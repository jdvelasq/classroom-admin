import os

from admin._intern import clone_github_repo, get_disk_repos, get_github_repos


def clone_github_repos(org_name):

    if not os.path.exists("../repos/"):
        os.makedirs("../repos/")

    github_repos = get_github_repos(org_name)
    disk_repos = get_disk_repos()

    missing_repos = [
        github_repo for github_repo in github_repos if github_repo not in disk_repos
    ]

    missing_repos = sorted(missing_repos)

    n_missing_repos = len(missing_repos)

    if n_missing_repos == 0:
        print("\n\nAll github repos already exist in disk.\n\n")
        return
    else:
        print(f"\n\n{n_missing_repos} missing repos in disk:\n")

    for index, repo_name in enumerate(missing_repos):
        print(f"  {1+index:03d} of {n_missing_repos}: {org_name}/{repo_name}")
        clone_github_repo(org_name, repo_name)
    print()
