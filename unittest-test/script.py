import unittest


class TestsContainer(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(1+1, 2)

    def test_mul(self):
        self.assertEqual(1*1, 1)


def make_test_function(a, b):
    def test(self):
        self.assertEqual(a, b)
    return test


if __name__ == '__main__':
    test_func = make_test_function(1-1, 0)
    setattr(TestsContainer, 'test_sub', test_func)
    unittest.main()
