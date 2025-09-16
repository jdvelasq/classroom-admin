# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface for thesaurus descriptor operations."""
import readline
import rlcompleter  # type: ignore

readline.parse_and_bind("bind ^I rl_complete")
import fixer.constants
from fixer.actions_shell import ActionsShell
from fixer.base_shell import BaseShell
from fixer.colorized_prompt import make_colorized_prompt
from fixer.course_shell import CourseShell
from fixer.descriptiva_shell import DescriptivaShell
from fixer.fundamentos_shell import FundamentosShell
from fixer.predictiva_shell import PredictivaaShell
from fixer.student_cmd import execute_student_command


class MainShell(BaseShell):

    intro = "Welcome. Type help or ? to list commands.\n"

    prompt = make_colorized_prompt("fixer:none:none:none")

    def do_actions(self, arg):
        """Run actions."""
        ActionsShell().update_prompt().cmdloop()
        self.update_prompt()
        self.do_help(arg)

    def do_course(self, arg):
        """Set course."""
        CourseShell().cmdloop()
        self.update_prompt()
        self.do_help(arg)

    def do_assigment(self, arg):
        """Set assigment."""
        if fixer.constants.course == "descriptiva":
            DescriptivaShell().update_prompt().cmdloop()
        elif fixer.constants.course == "predictiva":
            PredictivaaShell().update_prompt().cmdloop()
        elif fixer.constants.course == "fundamentos":
            FundamentosShell().cmdloop()
        self.update_prompt()
        self.do_help(arg)

    def do_student(self, arg):
        """Set student."""
        execute_student_command()
        self.update_prompt()
        self.do_help(arg)
