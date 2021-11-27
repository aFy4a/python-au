# Linked List

+ [Middle of the Linked List](#Middle-of-the-Linked-List)

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.middleNode([]), [])

    def test_odd_amount(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.middleNode(self.solution.create_single_linked_list([1, 2, 3, 4, 5]))), [3, 4, 5])

    def test_even_amount(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.middleNode(self.solution.create_single_linked_list([1, 2, 3, 4]))), [3, 4])
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
    def middleNode(self, head):
        second_head = head
        i = 0
        while second_head:
            second_head = second_head.next
            i += 1
        for j in range (i // 2):
            head = head.next

        return head

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