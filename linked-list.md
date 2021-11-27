# Linked List

+ [Reverse Linked List](#Reverse-Linked-List)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.reverseList([]), [])

    def test_one_value(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.reverseList(self.solution.create_single_linked_list([1]))), [1])

    def test_many_values(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.reverseList(self.solution.create_single_linked_list([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
```
</blockquote></details>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{} -> {}'.format(self.val, self.next)

class Solution:
    def reverseList(self, head):
        if head != []:
            reversed_head = None
            while head:
                to_check_next = head.next
                head.next = reversed_head
                reversed_head = head
                head = to_check_next
            return reversed_head
        return[]

    def create_single_linked_list(self, values):
        if len(values) > 0:
            previous_node = ListNode(values[len(values)-1])
            for i in range(0, len(values) - 1):
                next_node = ListNode(values[len(values) - i - 2], previous_node)
                previous_node = next_node
            return previous_node
        else: return []


    def get_linked_list_values(self, head):
        result = []
        if head != []:
            cur = head
            while cur != None:
                result.append(cur.val)
                cur = cur.next
        return result
```