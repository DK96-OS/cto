"""Testing Names create_new_file_name Methods"""
import pytest

from files.names import create_new_file_name


def test_create_new_file_name_empty_str_returns_suffix():
    assert create_new_file_name('', '-o') == '-o'


def test_create_new_file_name_empty_suffix_returns_name():
    assert create_new_file_name('name', '') == 'name'


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("file", "file-o"),
        ("input_file", "input_file-o"),
    ]
)
def test_create_new_file_name_no_file_ext_returns_name(test_input, expected):
    assert create_new_file_name(test_input, '-o') == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("input_file.txt", "input_file-o.txt"),
        ("input_file.cto", "input_file-o.cto"),
    ]
)
def test_create_new_file_name_with_file_ext_returns_name(test_input, expected):
    assert create_new_file_name(test_input, '-o') == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("input_file.tar.gz", "input_file.tar-o.gz"),
    ]
)
def test_create_new_file_name_weird_file_ext_returns_name(test_input, expected):
    assert create_new_file_name(test_input, '-o') == expected
