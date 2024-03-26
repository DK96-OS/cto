import unittest

from tests.cto_samples.assertions import assert_sample_expectations

_sample_prefix = 'challenge/challenge_'
_sample_count = 2


class TestChallenges(unittest.TestCase):

    def test_challenge_1(self):
        assert_sample_expectations(self, _sample_prefix, 1)

    def test_challenge_2(self):
        assert_sample_expectations(self, _sample_prefix, 2)


if __name__ == '__main__':
    unittest.main()
