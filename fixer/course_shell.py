# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
import fixer.constants
from fixer.base_shell import BaseShell
from fixer.colorized_prompt import make_colorized_prompt


class CourseShell(BaseShell):

    prompt = make_colorized_prompt("fixer:none:none:none")

    def do_fundamentos(self, arg):
        """set course to fundamentos."""

        fixer.constants.course = "fundamentos"
        fixer.constants.assignment = None
        return True

    def do_predictiva(self, arg):
        """set course to predictiva."""

        fixer.constants.course = "predictiva"
        fixer.constants.assignment = None
        return True

    def do_descriptiva(self, arg):
        """set course to descriptiva."""

        fixer.constants.course = "descriptiva"
        fixer.constants.assignment = None
        return True
