"""Testing File Validation Methods.
"""
import pytest
from pathlib import Path

from commit_text_organizer.file_validation import validate_input_file, validate_name


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("file_name", "file_data"),
        ("file_name12", "file_data"),
    ]
)
def test_validate_input_file_returns_data(test_input, expect):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: "file_data")
        assert validate_input_file(test_input) == expect


def test_validate_input_file_does_not_exist_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        try:
            validate_input_file("file_name")
            assert False
        except SystemExit:
            assert True


def test_validate_input_file_is_empty_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: "")
        try:
            validate_input_file("file_name")
            assert False
        except SystemExit:
            assert True


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("file_name", "file_data"),
        ("file_name12", "file_data"),
    ]
)
def test_validate_input_file_is_empty_returns_none(test_input, expect):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: expect)
        assert validate_input_file(test_input) == expect


@pytest.mark.parametrize(
    "test_input",
    [
        (None),
        (4),
        ({}),
        ([]),
        (""),
        (" "),
        ("\n"),
    ]
)
def test_validate_name_returns_false(test_input):
    assert not validate_name(test_input)


@pytest.mark.parametrize(
    "test_input",
    [
        ("1"),
        ("a"),
        ("test"),
    ]
)
def test_validate_name_returns_true(test_input):
    assert validate_name(test_input)
