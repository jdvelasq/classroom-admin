from admin._intern import get_disk_repos, pull_github_repo
from admin._intern.git import GitError


def pull_github_repos():

    disk_repos = get_disk_repos()

    n_disk_repos = len(disk_repos)

    if n_disk_repos == 0:
        print("\n\nNo repos in disk to pull.\n\n")
        return
    else:
        print(f"\n\nPulling {n_disk_repos} repos from github:\n")

    for index, repo_name in enumerate(disk_repos):
        
        print(f"  {1+index:03d} of {n_disk_repos}: {repo_name}")

        try:
            pull_github_repo(repo_name)
        except GitError as error:
            print(f"    ! failed to pull {repo_name}: {error}")

    print()
