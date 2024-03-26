import unittest

from tests.cto_samples.assertions import assert_sample_expectations

# The Sample Prefix points to the input and output files
_sample_prefix = 'generation/generation_'
_sample_count = 1


class TestGeneration(unittest.TestCase):

    def test_sample_1(self):
        assert_sample_expectations(self, _sample_prefix, 1)

    def test_sample_2(self):
        assert_sample_expectations(self, _sample_prefix, 2)


if __name__ == '__main__':
    unittest.main()
