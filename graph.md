# Graph

+ [Course Schedule](#Course_Schedule)

## Course Schedule

https://leetcode.com/problems/course-schedule/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cycle(self):
        self.assertEqual(self.solution.canFinish(3, [[0, 1], [1, 2], [2, 1]]), False)

    def test_not_cycle(self):
        self.assertEqual(self.solution.canFinish(4, [[1, 0], [2, 1], [3, 2]]), True)
```
</blockquote></details>

```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(v):
            if visit[v] == -1:
                return False
            if visit[v] == 1:
                return True

            visit[v] = -1
            for i in graph[v]:
                if not dfs(i):
                    return False
            visit[v] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
```