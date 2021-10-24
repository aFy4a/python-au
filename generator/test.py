import unittest
from solution import Solution

class TestSortedSquares(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.solution.sortedSquares([]), [])

    def test_negative_nums(self):
        self.assertEqual(self.solution.sortedSquares([-10, -5, -3]), [9, 25, 100])

    def test_positive_nums(self):
        self.assertEqual(self.solution.sortedSquares([2, 4, 6]), [4, 16, 36])

    def test_mixed_nums(self):
        self.assertEqual(self.solution.sortedSquares([-10, -4, -1, 0, 2, 4, 6]), [0, 1, 4, 16, 16, 36, 100])

if __name__ == "__main__":
    unittest.main()