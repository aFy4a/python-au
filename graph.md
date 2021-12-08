# Graph

+ [Number of Islands](#Number-of-Islands)

## Number of Islands

https://leetcode.com/problems/number-of-islands/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one_value_1(self):
        self.assertEqual(self.solution.numIslands([["1"]]), 1)

    def test_one_value_0(self):
        self.assertEqual(self.solution.numIslands([["0"]]), 0)

    def test_null_island(self):
        self.assertEqual(self.solution.numIslands([["0","0","0","0","0"], ["0","0","0","0","0"], ["0","0","0","0","0"], ["0","0","0","0","0"]]), 0)

    def test_one_island(self):
        self.assertEqual(self.solution.numIslands([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]), 1)

    def test_many_islands(self):
        self.assertEqual(self.solution.numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]), 3)
```
</blockquote></details>

```python
class Solution:
    def numIslands(self, grid):
        self.check = [0] * len(grid)
        for i in range(len(grid)):
            self.check[i] = [0] * len(grid[0])

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.check[i][j] == 0 and grid[i][j] == "1":
                    result += 1
                    self.dfs(i, j, grid)
        return result

    def dfs(self, x, y, grid):
        self.check[x][y] = 1
        if x > 0 and grid[x - 1][y] == "1" and self.check[x - 1][y] == 0:
            self.dfs(x - 1, y, grid)
        if y > 0 and grid[x][y - 1] == "1" and self.check[x][y - 1] == 0:
            self.dfs(x, y - 1, grid)
        if x < len(grid) - 1 and grid[x + 1][y] == "1" and self.check[x + 1][y] == 0:
            self.dfs(x + 1, y, grid)
        if y < len(grid[0]) - 1 and grid[x][y + 1] == "1" and self.check[x][y + 1] == 0:
            self.dfs(x, y + 1, grid)
```