from admin._intern import get_disk_repos, push_github_repo
from admin._intern.git import GitError


def push_github_repos(message="Update from classroom-admin"):

    disk_repos = get_disk_repos()

    n_disk_repos = len(disk_repos)

    if n_disk_repos == 0:
        print("\n\nNo repos in disk to push.\n\n")
        return
    else:
        print(f"\n\nPushing {n_disk_repos} repos to github:\n")

    for index, repo_name in enumerate(disk_repos):
        print(f"  {1+index:03d} of {n_disk_repos}: {repo_name}")

        try:
            push_github_repo(repo_name, message)
        except GitError as error:
            print(f"    ! failed to push {repo_name}: {error}")

    print()
