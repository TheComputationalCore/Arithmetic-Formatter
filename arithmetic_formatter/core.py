"""
Core formatting logic for the Arithmetic Formatter project.

This module contains the main function `arithmetic_arranger`,
which formats arithmetic problems vertically and side-by-side.
"""

from typing import List


def arithmetic_arranger(problems: List[str], show_answers: bool = False) -> str:
    """
    Arrange arithmetic problems vertically and side-by-side.

    Parameters
    ----------
    problems : list of str
        The arithmetic problems, each in the form "num1 operator num2".
    show_answers : bool, optional
        Whether to display the answers under each problem.

    Returns
    -------
    str
        A formatted, multi-line string displaying the arranged problems.

    Raises
    ------
    ValueError
        For invalid operators, too many problems, non-digit values,
        or improperly formatted inputs.
    """

    # Validate number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Validate operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Validate numeric values
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Validate number length
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        # Build formatted rows
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + num2.rjust(width - 1))
        dash_row.append("-" * width)

        if show_answers:
            result = str(eval(num1 + operator + num2))
            answer_row.append(result.rjust(width))

    # Combine rows
    arranged = "    ".join(top_row) + "\n"
    arranged += "    ".join(bottom_row) + "\n"
    arranged += "    ".join(dash_row)

    if show_answers:
        arranged += "\n" + "    ".join(answer_row)

    return arranged
