# Design

+ [Implement Queue using Stacks](#Implement-Queue-using-Stacks)

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import MyQueue

class TestImplementQueueUsingStacks(unittest.TestCase):
    def setUp(self):
        self.solution = MyQueue()

    def test_push(self):
        obj = MyQueue()
        obj.push(2)
        self.assertEqual(obj.peek(), 2)

    def test_peep(self):
        obj = MyQueue()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        self.assertEqual(obj.peek(), 5)

    def test_pop(self):
        obj = MyQueue()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        self.assertEqual(obj.pop(), 5)

    def test_pop_peep(self):
        obj = MyQueue()
        obj.push(5)
        obj.push(6)
        obj.push(3)
        obj.pop()
        self.assertEqual(obj.peek(), 6)

    def test_empty_true(self):
        obj = MyQueue()
        self.assertEqual(obj.empty(), True)

    def test_empty_false(self):
        obj = MyQueue()
        obj.push(2)
        self.assertEqual(obj.empty(), False)
```
</blockquote></details>

```python
class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        f = self.data[0]
        self.data = self.data[1:]
        return f

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        if len(self.data):
            return False
        return True
```