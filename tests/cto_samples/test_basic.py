import unittest

from tests.cto_samples.assertions import assert_sample_expectations

# The Sample Prefix points to the input and output files
_sample_prefix = 'basic/basic_'
_sample_count = 5


class TestBasic(unittest.TestCase):

    def test_sample_1(self):
        assert_sample_expectations(self, _sample_prefix, 1)

    def test_sample_2(self):
        assert_sample_expectations(self, _sample_prefix, 2)

    def test_sample_3(self):
        assert_sample_expectations(self, _sample_prefix, 3)

    def test_sample_4(self):
        assert_sample_expectations(self, _sample_prefix, 4)

    def test_sample_5(self):
        assert_sample_expectations(self, _sample_prefix, 5)


if __name__ == '__main__':
    unittest.main()
