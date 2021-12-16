# Linked List

+ [Merge Two Sorted Lists](#Merge-Two-Sorted-Lists)

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_empty_list(self):
        self.assertEqual(self.solution.mergeTwoLists([], []), [])

    def test_first_empty(self):
        self.assertEqual(self.get_linked_list_values(self.solution.mergeTwoLists([], self.create_single_linked_list([1, 2, 3]))), [1, 2, 3])

    def test_second_empty(self):
        self.assertEqual(self.get_linked_list_values(self.solution.mergeTwoLists(self.create_single_linked_list([1, 2, 3]), [])), [1, 2, 3])

    def test_two_lists(self):
        self.assertEqual(self.get_linked_list_values(self.solution.mergeTwoLists(self.create_single_linked_list([1, 2, 3]), self.create_single_linked_list([1, 3, 4]))), [1, 1, 2, 3, 3, 4])

    def create_single_linked_list(self, values):
        if len(values) > 0:
            previous_node = ListNode(values[len(values) - 1])
            for i in range(0, len(values) - 1):
                next_node = ListNode(values[len(values) - i - 2], previous_node)
                previous_node = next_node
            return previous_node
        else:
            return []

    def get_linked_list_values(self, head):
        result = []
        if head != []:
            cur = head
            while cur != None:
                result.append(cur.val)
                cur = cur.next
        return result
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
    def mergeTwoLists(self, l1, l2):
        if l1 == [] and l2 == []:
            return []
        if l1 == []:
            return l2
        if l2 == []:
            return l1

        result = ListNode()
        test = result

        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                test.next = l2
                l2 = l2.next
            elif l2.val > l1.val:
                test.next = l1
                l1 = l1.next
            test = test.next

        if l1 != None:
            test.next = l1
        if l2 != None:
            test.next = l2

        return result.next
```