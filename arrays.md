# Arrays

+ [Squares of a Sorted Array](#Squares-of-a-Sorted-Array)

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

<details><summary>Test case</summary><blockquote>

```python
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
```
</blockquote></details>

```python
def sortedSquares(self, nums):
    result = []
    if len(nums) > 0:
        right = 0

        while right < len(nums) and nums[right] < 0:
            right += 1

        left = right - 1

        while left >= 0 and right < len(nums):
            if abs(nums[right]) < abs(nums[left]):
                result.append(nums[right]**2)
                right += 1
            else:
                result.append(nums[left]**2)
                left -= 1
        while left >= 0:
            result.append(nums[left]**2)
            left -= 1
        while right < len(nums):
            result.append(nums[right]**2)
            right += 1

    return result
```
