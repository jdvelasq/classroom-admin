import subprocess


class GitError(RuntimeError):
    """Raised when a `git` command fails, with stderr included in the message."""


def run_git(repo_path, args):
    """Run a `git` command inside `repo_path`, raising GitError with stderr if it fails."""

    result = subprocess.run(
        ["git", "-C", repo_path, *args], capture_output=True, text=True
    )

    if result.returncode != 0:
        raise GitError(result.stderr.strip() or f"git {' '.join(args)} failed")

    return result.stdout
