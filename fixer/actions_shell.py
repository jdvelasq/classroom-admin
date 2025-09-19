# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
import subprocess

import fixer.constants
from fixer.base_shell import BaseShell
from fixer.colorized_prompt import make_colorized_prompt

org_mapping = {
    "descriptiva": "2025-2-descriptiva",
    "predictiva": "2025-2-predictiva",
    "fundamentos": "2025-2-fundamentos",
}


def check_inputs_are_ok():
    """Check inputs."""

    if fixer.constants.course is None:
        print("Please set the course first.")
        return False

    if fixer.constants.assignment is None:
        print("Please set the assignment first.")
        return False

    if fixer.constants.student is None:
        print("Please set the student first.")
        return False

    return True


class ActionsShell(BaseShell):

    prompt = make_colorized_prompt("fixer:none:none:none")

    def do_create(self, arg):
        """Create a new student repository."""

        if not check_inputs_are_ok():
            return True

        course = fixer.constants.course
        prefix = fixer.constants.prefix
        student = fixer.constants.student
        template = fixer.constants.template

        repo_name = f"{prefix}-{student}"

        org = org_mapping[course]
        org_repo = f"{org}/{repo_name}"
        org_template = f"{org}/{template}"

        result = subprocess.run(
            [
                "gh",
                "repo",
                "create",
                org_repo,
                "--public",
                "--template",
                org_template,
                "-y",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )

        if result.returncode != 0:
            # print()
            print("  Create command returns an error.")
        else:
            # print()
            print(f"  Created: {org_repo}")

        return True

    def do_delete(self, arg):
        """Delete the student repository."""

        if not check_inputs_are_ok():
            return True

        course = fixer.constants.course
        prefix = fixer.constants.prefix
        student = fixer.constants.student

        org = org_mapping[course]

        repo_name = f"{prefix}-{student}"
        org_repo = f"{org}/{repo_name}"

        # cmd = f'gh repo delete "{org_repo}" --yes >/dev/null 2>&1'

        result = subprocess.run(
            ["gh", "repo", "delete", org_repo, "--yes"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )

        if result.returncode != 0:
            print("  Delete command returns an error.")
        else:
            print(f"  Deleted: {org_repo}")

        return True

    def do_grant(self, arg):
        """Set write permission for the student."""

        if not check_inputs_are_ok():
            return True

        course = fixer.constants.course
        prefix = fixer.constants.prefix
        student = fixer.constants.student
        template = fixer.constants.template

        repo_name = f"{prefix}-{student}"
        org = org_mapping[course]
        org_repo = f"{org}/{repo_name}"

        result = subprocess.run(
            [
                "gh",
                "api",
                "-X",
                "PUT",
                "-H",
                "Accept: application/vnd.github+json",
                f"/repos/{org_repo}/collaborators/{student}",
                "-f",
                "permission=push",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )

        if result.returncode != 0:
            # print()
            print("  Grant command returns an error.")
        else:
            # print()
            print(f"  Granted: {org_repo}")

        return True
