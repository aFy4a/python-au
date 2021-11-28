# Design

+ [Min Stack](#Min_Stack)

## Min Stack

https://leetcode.com/problems/min-stack/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import MinStack

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = MinStack()

    def test_push(self):
        obj = MinStack()
        obj.push(2)
        self.assertEqual(obj.top(), 2)

    def test_top(self):
        obj = MinStack()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        self.assertEqual(obj.top(), 3)

    def test_pop(self):
        obj = MinStack()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        obj.pop()
        self.assertEqual(obj.top(), 6)

    def test_min(self):
        obj = MinStack()
        obj.push(5)
        obj.push(3)
        obj.push(6)
        self.assertEqual(obj.getMin(), 3)

    def test_min_pop(self):
        obj = MinStack()
        obj.push(4)
        obj.push(0)
        obj.push(-5)
        obj.pop()
        self.assertEqual(obj.getMin(), 0)
```
</blockquote></details>

```python
import sys
class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        if len(self.data) == 0:
            return sys.maxsize
        return self.data[-1][1]
```