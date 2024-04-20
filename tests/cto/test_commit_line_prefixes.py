import unittest

from commit_text_organizer.commit_line_prefixes import map_line_prefix


class TestCommitLinePrefixes(unittest.TestCase):
    """Test that commit messages have the correct line prefixes.
    """

    def test_update_line_no_space(self):
        expected = "* Update README.md - reformat file"
        line = "*u README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line),
        )
        line = "*U README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line)
        )

    def test_update_line_with_space(self):
        expected = "* Update README.md - reformat file"
        line = "* U README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line)
        )

    def test_update_line_extra_prefix_no_space(self):
        expected = "* Update README.md - reformat file"
        line = "*Up README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line)
        )
        line = "*up README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line)
        )

    def test_update_line_extra_prefix_with_space(self):
        expected = "* Update README.md - reformat file"
        line = "* Up README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line)
        )
        line = "* up README.md - reformat file"
        self.assertEqual(
            expected, map_line_prefix(line)
        )

    def test_update_line_invalid_prefix(self):
        line = "* X README.md - reformat file"
        self.assertIsNone(
            map_line_prefix(line)
        )

    def test_update_line_already_valid_prefix(self):
        line = "* Update README.md - reformat file"
        self.assertIsNone(
            map_line_prefix(line)
        )


if __name__ == '__main__':
    unittest.main()
