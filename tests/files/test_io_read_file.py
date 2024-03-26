"""Testing IO read_file Method"""
from files.io import read_file
from tests.files import mock_file_exists, mock_file_does_not_exist


def test_read_file_it_exists_returns_none():
    with mock_file_exists():
        assert read_file('file_name') == 'file_text'


def test_read_file_does_not_exist_raises_exit():
    with mock_file_does_not_exist():
        try:
            read_file('file_name')
            assert False
        except SystemExit:
            assert True
