import fixer.constants
from fixer.colorized_input import colorized_input


def execute_student_command():

    print()

    student = colorized_input(". username > ").strip()
    fixer.constants.student = student

    print()
