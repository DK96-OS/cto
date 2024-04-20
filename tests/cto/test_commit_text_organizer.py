import unittest

from commit_text_organizer.commit_text_organizer import CommitTextOrganizer


class TestCommitTextOrganizer(unittest.TestCase):

	def setUp(self) -> None:
		self.inst = CommitTextOrganizer()

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
		# Check output
		result = self.inst.output_all_groups()
		self.assertEqual(result, f"Pull Requests:\n* {input_text}\n")


if __name__ == '__main__':
	unittest.main()
