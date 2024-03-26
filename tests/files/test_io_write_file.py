"""Testing IO write_file Method"""
from files.io import write_file


def test_write_file_empty_data_returns_false():
    assert write_file('file_name', '') == False


def test_write_file_empty_file_name_returns_false():
    assert write_file('', 'data') == False


def test_write_file_valid_inputs_returns_true():
    assert write_file('file_name', 'data') == True
