import unittest
from solution import Solution
import generator_md as gmd

class TestSortedSquares(unittest.TestCase):
    ##Tests solution.py

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

    ##Tests generator_md.py

    def test_get_md_headline(self):
        self.assertEqual(gmd.get_md_headline('Arrays'), '# Arrays\n')

    def test_get_md_head(self):
        self.assertEqual(gmd.get_md_head('Squares of a Sorted Array'), '## Squares of a Sorted Array\n')

    def test_get_md_anchor(self):
        self.assertEqual(gmd.get_md_anchor('Squares of a Sorted Array'), '+ [Squares of a Sorted Array](#Squares-of-a-Sorted-Array)')

    def test_get_md_link(self):
        self.assertEqual(gmd.get_md_link('asdf'), 'asdf')

    def test_get_md_code_block(self):
        self.assertEqual(gmd.get_md_code_block('qwert'), '```python\nqwert\n```\n')

    def test_get_md_details(self):
        self.assertEqual(gmd.get_md_details('title', 'data'), '<details><summary>title</summary><blockquote>\n\ndata\n</blockquote></details>\n')

if __name__ == "__main__":
    unittest.main()