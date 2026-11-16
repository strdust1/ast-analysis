import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from hello import greet


def test_greet_returns_expected_string():
    assert greet("World") == "Hello, World!"