# Graph

+ [Course Schedule II](#Course-Schedule-II)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cycle(self):
        self.assertEqual(self.solution.findOrder(3, [[0, 1], [1, 2], [2, 1]]), [])

    def test_two_vertex(self):
        self.assertEqual(self.solution.findOrder(2, [[0, 1]]), [1, 0])

    def test_many_vertex(self):
        self.assertEqual(self.solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 2, 1, 3])
```
</blockquote></details>

```python
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        answer = []
        for x, y in prerequisites:
            graph[y].append(x)

        def check_dfs(v):
            if visit[v] == -1:
                return False
            if visit[v] == 1:
                return True

            visit[v] = -1
            for i in graph[v]:
                if not check_dfs(i):
                    return False
            visit[v] = 1
            return True

        for i in range(numCourses):
            if not check_dfs(i):
                return []
        visit = [0 for _ in range(numCourses)]
        def dfs(v):
            visit[v] = 1
            for i in graph[v]:
                if visit[i] == 0:
                    dfs(i)
            answer.append(v)
        for i in range(numCourses):
            if visit[i] == 0:
                dfs(i)
        answer.reverse()
        return answer
```