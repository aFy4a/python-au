# Design

+ [Implement Stack using Queues](#Implement-Stack-using-Queues)

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import MyStack

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = MyStack()

    def test_push(self):
        obj = MyStack()
        obj.push(2)
        self.assertEqual(obj.top(), 2)

    def test_top(self):
        obj = MyStack()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        self.assertEqual(obj.top(), 3)

    def test_pop(self):
        obj = MyStack()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        self.assertEqual(obj.pop(), 3)

    def test_pop_top(self):
        obj = MyStack()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        obj.pop()
        self.assertEqual(obj.top(), 6)

    def test_empty_true(self):
        obj = MyStack()
        self.assertEqual(obj.empty(), True)

    def test_empty_false(self):
        obj = MyStack()
        obj.push(2)
        self.assertEqual(obj.empty(), False)
```
</blockquote></details>

```python
class MyStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        f = self.data[-1]
        self.data.pop()
        return f

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        if len(self.data):
            return False
        return True
```