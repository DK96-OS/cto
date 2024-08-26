"""Testing Argument Parsing Module.
"""
from pathlib import Path
import pytest

from commit_text_organizer.argument_data import ArgumentData
from commit_text_organizer.argument_parser import _validate_arguments, validate_input
from commit_text_organizer.input_data import InputData


@pytest.mark.xfail(raises=SystemExit, reason="invalid arguments")
@pytest.mark.parametrize(
    "test_input",
    [
        ([]),
        ([""]),
        ([" "]),
        (["input_file", '-a']),
    ]
)
def test_validate_arguments_raises_value_error(test_input):
    with pytest.raises(SystemExit) as exit_info:
        _validate_arguments(test_input)
    assert exit_info.type is SystemExit


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("input_file", ArgumentData("input_file")),
    ]
)
def test_validate_arguments_returns_data(test_input, expect):
    assert _validate_arguments(test_input) == expect


@pytest.mark.xfail(raises=SystemExit, reason="invalid arguments")
@pytest.mark.parametrize(
    "test_input",
    [
        ([]),
        ([""]),
        ([" "]),
        (["input_file", '-a']),
    ]
)
def test_validate_input_arguments_raises_value_error(test_input):
    with pytest.raises(SystemExit) as exit_info:
        validate_input(test_input)
    assert exit_info.type is SystemExit


@pytest.mark.parametrize(
    "test_input,expect",
    [
        (["input_file"], InputData("input data")),
    ]
)
def test_validate_input_arguments_returns_data(test_input, expect):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: 'input data')
        assert validate_input(test_input) == expect
