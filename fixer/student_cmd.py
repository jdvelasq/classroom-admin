import fixer.constants
from fixer.colorized_input import colorized_input


def execute_student_command(arg=None):

    if arg is None:
        print()
        student = colorized_input(". username > ").strip()
        fixer.constants.student = student
        print()
    else:
        fixer.constants.student = arg.strip()
