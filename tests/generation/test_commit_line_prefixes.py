import unittest

from text.generation.commit_line_prefixes import update_line


class TestCommitLinePrefixes(unittest.TestCase):
    """Test that commit messages have the correct line prefixes."""

    def test_update_line_no_space(self):
        expected = "* Update README.md - reformat file"
        line = "*u README.md - reformat file"
        self.assertEquals(
            expected, update_line(line),
        )
        line = "*U README.md - reformat file"
        self.assertEquals(
            expected, update_line(line)
        )

    def test_update_line_with_space(self):
        expected = "* Update README.md - reformat file"
        line = "* U README.md - reformat file"
        self.assertEquals(
            expected, update_line(line)
        )

    def test_update_line_extra_prefix_no_space(self):
        expected = "* Update README.md - reformat file"
        line = "*Up README.md - reformat file"
        self.assertEquals(
            expected, update_line(line)
        )
        line = "*up README.md - reformat file"
        self.assertEquals(
            expected, update_line(line)
        )

    def test_update_line_extra_prefix_with_space(self):
        expected = "* Update README.md - reformat file"
        line = "* Up README.md - reformat file"
        self.assertEquals(
            expected, update_line(line)
        )
        line = "* up README.md - reformat file"
        self.assertEquals(
            expected, update_line(line)
        )

    def test_update_line_invalid_prefix(self):
        line = "* X README.md - reformat file"
        self.assertIsNone(update_line(line))

    def test_update_line_already_valid_prefix(self):
        line = "* Update README.md - reformat file"
        self.assertIsNone(update_line(line))


if __name__ == '__main__':
    unittest.main()
