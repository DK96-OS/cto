"""Testing the Text Package Init Method"""

from text import process_with_cto as cto


def test_cto_empty_str_returns_none():
    assert cto('') is None

def test_cto_space_str_returns_none():
    assert cto(' ') is None

def test_cto_header_returns_header():
    assert cto('Header:') == 'Header:\n'

def test_cto_commit_line_returns_line():
    assert cto('*u my_file.py') == '* Update my_file.py\n'

def test_cto_two_commit_lines_returns_lines():
    expected = '* Update my_file.py\n* Update other_file.py\n'
    assert cto('*u my_file.py\n*u other_file.py') == expected

def test_cto_header_with_two_commit_lines_returns_all():
    expected = 'Header:\n* Update my_file.py\n* Update other_file.py\n'
    assert cto('Header:\n*u my_file.py\n*u other_file.py') == expected
