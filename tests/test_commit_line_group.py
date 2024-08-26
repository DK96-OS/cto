import unittest

from commit_text_organizer.commit_line_group import CommitLineGroup


input_text_1 = """
* Message 1
* Message 2 - 6
""".strip()

input_text_2 = """
* Message 2 - 1234
* Message 2 - 5
""".strip()

input_text_3 = """
* Alternate Challenge - z
* Alternate Challenge - a
* Alternate Challenge - n
""".strip()


class TestCommitTextGroup(unittest.TestCase):

	def setUp(self):
		self.header_1 = "* Header 1:"
		self.header_1_processed = "Header 1:"
		self.header_2 = "Header 2:"
		self.lines_1 = input_text_1.split('\n')
		self.lines_2 = input_text_2.split('\n')
		self.c_group_1 = CommitLineGroup(self.header_1, self.lines_1)
		self.c_group_2 = CommitLineGroup(self.header_2, self.lines_2)

	def test_initial_conditions(self):
		self.assertEqual(
			2, self.c_group_1.get_line_count()
		)
		self.assertEqual(
			2, self.c_group_2.get_line_count()
		)
		# Headers should match after processing
		self.assertEqual(
			9, len(self.c_group_1.get_header())
		)
		self.assertEqual(
			9, len(self.c_group_2.get_header())
		)

	def test_get_header_1(self):
		self.assertEqual(
			self.header_1_processed, self.c_group_1.get_header()
		)

	def test_get_header_none(self):
		group = CommitLineGroup(None, self.lines_1)
		self.assertEqual(
			"", group.get_header()
		)

	def test_add_line_group_1_then_autoprocess(self):
		self.assertTrue(
			self.c_group_1.add_line(self.lines_2[0])
		)
		self.assertEqual(
			3, self.c_group_1.get_line_count()
		)
		self.c_group_1.autoprocess()
		self.assertEqual(
			2, self.c_group_1.get_line_count()
		)

	def test_add_line_group_2_then_autoprocess(self):
		self.assertTrue(
			self.c_group_2.add_line(self.lines_1[1])
		)
		self.assertEqual(
			3, self.c_group_2.get_line_count()
		)
		self.c_group_2.autoprocess()
		self.assertEqual(
			1, self.c_group_2.get_line_count()
		)

	def test_add_line_group_2_after_autoprocess(self):
		self.c_group_2.autoprocess()
		self.assertEqual(
			1, self.c_group_2.get_line_count()
		)
		self.assertTrue(
			self.c_group_2.add_line(self.lines_2[0])
		)
		self.assertEqual(
			2, self.c_group_2.get_line_count()
		)
		# Run Autoprocess again
		self.c_group_2.autoprocess()
		self.assertEqual(
			1, self.c_group_2.get_line_count()
		)

	def test_get_line_count_group_3(self):
		cto = CommitLineGroup(None, input_text_3.split('\n'))
		self.assertEqual(
			3, cto.get_line_count()
		)
		cto.autoprocess()
		self.assertEqual(
			1, cto.get_line_count()
		)

	def test_string_method_group_1(self):
		initial_str = str(self.c_group_1)
		self.c_group_1.autoprocess()
		# Group 1 does not change from processing
		self.assertEqual(
			initial_str, str(self.c_group_1)
		)

	def test_string_method_group_2(self):
		initial_str = str(self.c_group_2)
		self.c_group_2.autoprocess()
		self.assertNotEqual(
			initial_str, str(self.c_group_2)
		)

	def test_string_method_group_3(self):
		cto = CommitLineGroup(None, input_text_3.split('\n'))
		initial_str = str(cto)
		cto.autoprocess()
		self.assertNotEqual(
			initial_str, str(cto)
		)

	def test_string_method_no_header(self):
		g = CommitLineGroup(None, self.lines_1)
		g.add_line(self.lines_1[1])
		result_lines = (str(g)).split('\n')
		self.assertEqual(
			3, len(result_lines)
		)
		self.assertEqual(
			"* Message 1", result_lines[0]
		)
		self.assertEqual(
			"* Message 2 - 6", result_lines[1]
		)
		self.assertEqual(
			"* Message 2 - 6", result_lines[2]
		)


def test_get_lines_as_commit_line_array_empty_returns_empty_list():
	inst = CommitLineGroup(None, [])
	assert inst.get_lines_as_commit_line_array() == []


def test_get_lines_as_str_array_empty_returns_empty_list():
	inst = CommitLineGroup(None, [])
	assert inst.get_lines_as_str_array() == []


def test_get_lines_as_str_array_single_element_returns_element():
	input_line = '*u my_file.py'
	expected_line = '* Update my_file.py'
	inst = CommitLineGroup(None, [input_line])
	assert inst.get_lines_as_str_array() == [expected_line]


def test_add_line_empty_str_returns_false():
	inst = CommitLineGroup(None, [])
	assert not inst.add_line('')


def test_add_line_unknown_type_returns_false():
	inst = CommitLineGroup(None, [])
	assert not inst.add_line(1)
