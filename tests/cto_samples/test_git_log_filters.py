import unittest

from tests.cto_samples.assertions import assert_sample_expectations

_sample_prefix = 'git_log_filter/git_log_filter_'
_sample_count = 1


class TestGitLogFilters(unittest.TestCase):

    def test_git_log_filter_1(self):
        assert_sample_expectations(self, _sample_prefix, 1)


if __name__ == '__main__':
    unittest.main()
