"""Testing Commit Line Module Class and Methods.
"""
import pytest
import unittest

from commit_text_organizer.commit_line import CommitLine, find_subject_separator, merge_lines


class TestCommitLine(unittest.TestCase):
    """ Testing the Commit Line Class.
    The Test setup includes a basic Commit Line input, consisting of a subject and content combined into a simple input.
    """

    def setUp(self) -> None:
        self.subjectA = "A Subject"
        self.contentA = "A Content"
        #
        self.subject = "Subject"
        self.content = "Content"
        self.input = "Subject - Content"
        self.commit_line = CommitLine(self.input)

    def test_get_line_input_returns_input(self):
        self.assertEqual(
            self.input,
            self.commit_line.get_input_line()
        )

    def test_get_subject_returns_subject(self):
        self.assertEqual(
            self.subject,
            self.commit_line.get_subject()
        )

    def test_get_subject_A_minus_returns_subject(self):
        self.assertEqual(
            self.subjectA,
            CommitLine(
                self.subjectA + ' - ' + self.contentA
            ).get_subject()
        )

    def test_get_subject_A_minus_no_space_returns_subject(self):
        self.assertEqual(
            self.subjectA,
            CommitLine(
                self.subjectA + '-' + self.contentA
            ).get_subject()
        )

    def test_get_subject_A_plus_returns_subject(self):
        self.assertEqual(
            self.subjectA,
            CommitLine(
                self.subjectA + ' + ' + self.contentA
            ).get_subject()
        )

    def test_get_subject_A_plus_returns_subject(self):
        self.assertEqual(
            self.subjectA,
            CommitLine(
                self.subjectA + '+' + self.contentA
            ).get_subject()
        )

    def test_get_subject_A_no_separator_returns_none(self):
        self.assertEqual(
            None, CommitLine(
                self.subjectA + ' ' + self.contentA
            ).get_subject()
        )

    def test_get_subject_empty_line_returns_none(self):
        self.assertEqual(
            None, CommitLine("").get_subject()
        )

    def test_get_content_commit_line_returns_content(self):
        self.assertEqual(
            self.content,
            self.commit_line.get_content()
        )

    def test_get_content_line_A_minus_returns_content(self):
        self.assertEqual(
            self.contentA,
            CommitLine(
                self.subjectA + ' - ' + self.contentA
            ).get_content()
        )

    def test_get_content_line_A_plus_returns_content(self):
        self.assertEqual(
            self.contentA,
            CommitLine(
                self.subjectA + ' + ' + self.contentA
            ).get_content()
        )

    def test_get_content_no_separator_returns_line(self):
        line = self.subjectA + ' ' + self.contentA
        self.assertEqual(
            line,
            CommitLine(
                self.subjectA + ' ' + self.contentA
            ).get_content()
        )

    def test_get_content_empty_line_returns_none(self):
        self.assertIsNone(
            CommitLine("").get_content()
        )


if __name__ == '__main__':
    unittest.main()


# pytests

cl1 = CommitLine('*u my_file.py - add method main')

cl2 = CommitLine('*u my_file.py - remove method main')

cl3 = CommitLine('*u my_file.py - add docs')


@pytest.mark.parametrize(
    "line1,line2,expected_content",
    [
        (cl1, cl2, '* Update my_file.py - add method main, remove method main'),
        (cl1, cl3, '* Update my_file.py - add method main, add docs'),
        (cl2, cl3, '* Update my_file.py - remove method main, add docs'),
    ]
)
def test_merge_lines(line1, line2, expected_content):
    result = merge_lines(line1, line2)
    assert str(result) == expected_content


def test_find_subject_separator_():
    test_input = '*u my_file - add method do_something'
    assert find_subject_separator(test_input) == 11


@pytest.mark.parametrize(
    "test_input",
    [
        '',
        'Header:',
        '*u file.txt',
        '*a',
        '2',
    ]
)
def test_find_subject_separator_without_one_returns_none(test_input):
    assert find_subject_separator(test_input) is None
