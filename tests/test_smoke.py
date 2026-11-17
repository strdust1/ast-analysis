import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from hello import one_plus_one


def test_one_plus_one_returns_2():
    assert one_plus_one() == 2