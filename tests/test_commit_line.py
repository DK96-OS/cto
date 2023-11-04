import unittest
from text.commit_line import CommitLine


class TestCommitLine(unittest.TestCase):

    def setUp(self) -> None:
        self.subjectA = "A Subject"
        self.contentA = "A Content"
        #
        self.subject = "Subject"
        self.content = "Content"
        self.input = "Subject - Content"
        self.commit_line = CommitLine(self.input)

    def test_get_line(self):
        self.assertEquals(
            self.input,
            self.commit_line.get_input_line()
        )

    def test_get_subject(self):
        self.assertEquals(
            self.subject,
            self.commit_line.get_subject()
        )

    def test_get_subject_A_minus(self):
        self.assertEquals(
            self.subjectA,
            CommitLine(
                self.subjectA + ' - ' + self.contentA
            ).get_subject()
        )
        # Also with no space around separator
        self.assertEquals(
            self.subjectA,
            CommitLine(
                self.subjectA + '-' + self.contentA
            ).get_subject()
        )

    def test_get_subject_A_plus(self):
        self.assertEquals(
            self.subjectA,
            CommitLine(
                self.subjectA + ' + ' + self.contentA
            ).get_subject()
        )
        # Also with no space around separator
        self.assertEquals(
            self.subjectA,
            CommitLine(
                self.subjectA + '+' + self.contentA
            ).get_subject()
        )

    def test_get_subject_A_no_separator(self):
        self.assertEquals(
            None, CommitLine(
                self.subjectA + ' ' + self.contentA
            ).get_subject()
        )

    def test_get_subject_empty(self):
        self.assertEquals(
            None, CommitLine("").get_subject()
        )

    def test_get_content(self):
        self.assertEquals(
            self.content,
            self.commit_line.get_content()
        )

    def test_get_content_A_minus(self):
        self.assertEquals(
            self.contentA,
            CommitLine(
                self.subjectA + ' - ' + self.contentA
            ).get_content()
        )

    def test_get_content_A_plus(self):
        self.assertEquals(
            self.contentA,
            CommitLine(
                self.subjectA + ' + ' + self.contentA
            ).get_content()
        )

    def test_get_content_no_separator(self):
        line = self.subjectA + ' ' + self.contentA
        self.assertEquals(
            line,
            CommitLine(
                self.subjectA + ' ' + self.contentA
            ).get_content()
        )

    def test_get_content_empty(self):
        self.assertIsNone(
            CommitLine("").get_content()
        )


if __name__ == '__main__':
    unittest.main()
