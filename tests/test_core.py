import pytest
from arithmetic_formatter.core import arithmetic_arranger


def test_basic_formatting():
    result = arithmetic_arranger(["32 + 8"])
    expected = "  32\n+  8\n----"
    assert result == expected


def test_with_answers():
    result = arithmetic_arranger(["32 + 8"], show_answers=True)
    expected = "  32\n+  8\n----\n  40"
    assert result == expected


def test_too_many_problems():
    problems = ["1 + 2"] * 6
    assert arithmetic_arranger(problems) == "Error: Too many problems."


def test_invalid_operator():
    assert arithmetic_arranger(["32 * 8"]) == "Error: Operator must be '+' or '-'."


def test_non_digit():
    assert arithmetic_arranger(["3a + 2"]) == "Error: Numbers must only contain digits."


def test_exceeds_digit_limit():
    assert arithmetic_arranger(["12345 + 2"]) == "Error: Numbers cannot be more than four digits."
