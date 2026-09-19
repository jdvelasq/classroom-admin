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
import _admin.constants
from _admin.actions_shell import ActionsShell
from _admin.base_shell import BaseShell
from _admin.colorized_prompt import make_colorized_prompt
from _admin.course_shell import CourseShell
from _admin.descriptiva_shell import DescriptivaShell
from _admin.fundamentos_shell import FundamentosShell
from _admin.predictiva_shell import PredictivaaShell
from _admin.student_cmd import execute_student_command


class MainShell(BaseShell):

    intro = "Welcome. Type help or ? to list commands.\n"
    prompt = make_colorized_prompt("fixer:none:none:none")

    def cmdloop(self, intro=None):
        if not self.cmdqueue:  # Only print help if not processing a batch
            self.do_help("")
        super().cmdloop(intro)

    def do_actions(self, arg):
        """Run actions."""

        shell = ActionsShell()
        if self.cmdqueue:
            cmd = self.cmdqueue.pop(0)
            shell.cmdqueue.append(cmd)
            shell.cmdloop()
        else:
            shell.do_help(arg)
            shell.update_prompt()
            shell.cmdloop()
            self.do_help(arg)

    def do_course(self, arg):
        """Set course."""
        shell = CourseShell()
        if self.cmdqueue:
            cmd = self.cmdqueue.pop(0)
            shell.cmdqueue.append(cmd)
            shell.cmdloop()
            self.update_prompt()
        else:
            shell.do_help(arg)
            shell.update_prompt()
            shell.cmdloop()
            self.update_prompt()
            self.do_help(arg)

    def do_assigment(self, arg):
        """Set assigment."""
        if _admin.constants.course == "descriptiva":
            shell = DescriptivaShell()
        elif _admin.constants.course == "predictiva":
            shell = PredictivaaShell()
        elif _admin.constants.course == "fundamentos":
            shell = FundamentosShell()
        else:
            print("Please set the course first.")
            return

        if self.cmdqueue:
            cmd = self.cmdqueue.pop(0)
            shell.cmdqueue.append(cmd)
            shell.cmdloop()
            self.update_prompt()
        else:
            shell.do_help(arg)
            shell.update_prompt()
            shell.cmdloop()
            self.update_prompt()
            self.do_help(arg)

    def do_student(self, arg):
        """Set student."""
        if self.cmdqueue:
            cmd = self.cmdqueue.pop(0)
            execute_student_command(cmd)
        else:
            execute_student_command()
            self.update_prompt()
            self.do_help(arg)

    def do_batch(self, arg):
        """Run commands from a file: batch <filename>"""
        try:
            with open(arg) as f:
                commands = f.readlines()

            commands = [
                line.strip()
                for line in commands
                if line.strip() and not line.strip().startswith("#")
            ]
            commands = " ".join(commands)
            commands = commands.split()
            commands = [cmd.strip() for cmd in commands if cmd.strip()]
            self.cmdqueue.extend(commands)
        except Exception as e:
            print(f"Batch error: {e}")
