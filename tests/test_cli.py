import subprocess
import sys
import os

def run_cli(args):
    """Helper to run the CLI command."""
    cmd = [sys.executable, "-m", "arithmetic_formatter.cli"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


def test_cli_basic():
    output = run_cli(["32 + 8"])
    assert "32" in output
    assert "+" in output
    assert "-" in output


def test_cli_answers():
    output = run_cli(["32 + 8", "--answers"])
    assert "40" in output
