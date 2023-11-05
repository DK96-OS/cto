import unittest
from commit_organizer import CommitTextOrganizer


class TestCommitTextOrganizer(unittest.TestCase):

	def test_empty_input_will_return_none(self):
		input_text = """"""
		organizer = CommitTextOrganizer()
		organizer.receive_data(input_text)
		organizer.autoprocess()
		self.assertIsNone(
			organizer.output_all_groups()
		)


if __name__ == '__main__':
	unittest.main()
