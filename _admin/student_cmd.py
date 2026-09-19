import _admin.constants
from _admin.colorized_input import colorized_input


def execute_student_command(arg=None):

    if arg is None:
        print()
        student = colorized_input(". username > ").strip()
        _admin.constants.student = student
        print()
    else:
        _admin.constants.student = arg.strip()
