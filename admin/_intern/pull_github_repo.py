from admin._intern.git import run_git


def pull_github_repo(repo_name):

    run_git(f"../repos/{repo_name}", ["pull", "--rebase"])
