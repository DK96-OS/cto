import unittest

from commit_text_organizer.commit_organizer import CommitOrganizer, process_with_cto
from commit_text_organizer.input_data import InputData


class TestCommitOrganizer(unittest.TestCase):

	def setUp(self) -> None:
		self.inst = CommitOrganizer()

	def test_empty_input_will_return_none(self):
		input_text = """"""
		self.inst.receive_data(input_text)
		self.inst.autoprocess()
		self.assertIsNone(
			self.inst.output_all_groups()
		)

	def test_receive_data_unknown_line_returns_none(self):
		input_text = "\n\n\nHello"
		self.inst.receive_data(input_text)
		self.inst.autoprocess()
		self.assertIsNone(
			self.inst.output_all_groups()
		)

	def test_add_pull_request_line_adds_group(self):
		input_text = "Debug Line Number (#8)"
		self.inst.add_pull_request_line(input_text)
		#
		self.assertEqual(1, len(self.inst.groups))
		self.assertIsNotNone(self.inst.pr_group)

	def test_add_pull_request_line_then_output_all_groups_returns_pr_group(self):
		input_text = "Debug Line Number (#8)"
		self.inst.add_pull_request_line(input_text)
		# Check instance state
		assert len(self.inst.groups) == 1
		assert self.inst.pr_group is not None
		# Check output
		result = self.inst.output_all_groups()
		self.assertEqual(result, f"Pull Requests:\n* {input_text}\n")

	def test_clear_after_receive_data(self):
		input_text = ""
		self.inst.receive_data(input_text)
		self.inst.clear()
		assert self.inst.groups == []
		assert self.inst.pr_group is None

	def test_clear_after_add_pr_line(self):
		self.inst.add_pull_request_line("PR (# 4)")
		self.inst.clear()
		assert self.inst.groups == []
		assert self.inst.pr_group is None


if __name__ == '__main__':
	unittest.main()


def cto(test_string: str):
	"""Wrap with InputData and call process_with_cto.
	"""
	return process_with_cto(InputData(test_string))

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
