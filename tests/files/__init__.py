"""Testing Files Package"""
from pathlib import Path
import pytest


def mock_file_exists():
    """"""
    mp = pytest.MonkeyPatch()
    mp.setattr(Path, 'exists', lambda _: True)
    mp.setattr(Path, 'read_text', lambda _: "file_text")
    return mp.context()


def mock_file_does_not_exist():
    """"""
    mp = pytest.MonkeyPatch()
    mp.setattr(Path, 'exists', lambda _: False)
    mp.setattr(Path, 'read_text', lambda _: "")
    return mp.context()
