import unittest

from commit_text_organizer.commit_line_group import CommitLineGroup
from commit_text_organizer.commit_line import CommitLine

input_text_challenge_2 = tuple("""
* Third Challenge-a,  c
* Third Challenge  -a,b
""".strip().split("\n"))


class TestCommitTextGroupChallenges(unittest.TestCase):

	def setUp(self):
		pass

	def test_input_challenge_2(self):
		lines = [
			CommitLine(x) for x in input_text_challenge_2
		]
		print([str(x) for x in lines])
		print([str(x.get_subject()) for x in lines])
		print([str(x.get_content()) for x in lines])

		cto = CommitLineGroup(None, input_text_challenge_2)
		cto.autoprocess()
		print(str(cto))
