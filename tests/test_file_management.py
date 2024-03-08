import pytest

from files.file_management import create_new_file_name


@pytest.mark.parametrize(
	'initial_name,suffix,expected',
	[
		('file', '_new', 'file_new'),
		('1', '_new', '1_new'),
		('file', '_1', 'file_1'),
	]
)
def test_create_new_file_name(initial_name, suffix, expected):
	assert create_new_file_name(initial_name, suffix) == expected


@pytest.mark.parametrize(
	'initial_name,suffix,expected',
	[
		('file.txt', '_new', 'file_new.txt'),
		('1.txt', '_new', '1_new.txt'),
		('file.txt', '_1', 'file_1.txt'),
	]
)
def test_create_new_file_name_txt(initial_name, suffix, expected):
	assert create_new_file_name(initial_name, suffix) == expected
