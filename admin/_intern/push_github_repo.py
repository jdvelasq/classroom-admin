from admin._intern.git import run_git
from admin._intern.pull_github_repo import pull_github_repo


def push_github_repo(repo_name, message="Update from classroom-admin"):

    repo_path = f"../repos/{repo_name}"

    run_git(repo_path, ["add", "--all"])

    if run_git(repo_path, ["status", "--porcelain"]).strip():
        run_git(repo_path, ["commit", "--message", message])

    pull_github_repo(repo_name)

    run_git(repo_path, ["push"])
