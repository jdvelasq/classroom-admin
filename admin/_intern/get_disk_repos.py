import glob
import os


def get_disk_repos():

    if not os.path.exists("../repos/"):
        return []
    repos = sorted(glob.glob("../repos/std-*"))
    repos = [os.path.basename(repo) for repo in repos]
    repos = sorted(repos)
    return repos
