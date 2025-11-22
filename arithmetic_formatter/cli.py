"""
Command-Line Interface for arithmetic_formatter.

Usage:
    arithmetic-formatter "32 + 8" "1 - 3801" --answers
"""

import argparse
from .core import arithmetic_arranger


def main():
    parser = argparse.ArgumentParser(
        description="Arrange arithmetic problems vertically."
    )

    parser.add_argument(
        "problems",
        nargs="+",
        help='Arithmetic problems like "32 + 8"',
    )

    parser.add_argument(
        "--answers",
        "-a",
        action="store_true",
        help="Display answers under the problems",
    )

    args = parser.parse_args()

    output = arithmetic_arranger(args.problems, show_answers=args.answers)
    print(output)


if __name__ == "__main__":
    main()
