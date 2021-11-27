# Linked List

+ [Sort List](#Sort_List)

## Sort List

https://leetcode.com/problems/sort-list/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_head(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sortList(self.solution.create_single_linked_list([]))), [])

    def test_positive_numb(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sortList(self.solution.create_single_linked_list([4, 1, 8, 5]))), [1, 4, 5, 8])

    def test_negative_num(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sortList(self.solution.create_single_linked_list([-4, -1, -8, -5]))), [-8, -5, -4, -1])

    def test_int_num(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sortList(self.solution.create_single_linked_list([-4, 5, 2, 0, -1]))), [-4, -1, 0, 2, 5])

    def test_int_num_repeat(self):
        self.assertEqual(self.solution.get_linked_list_values(
            self.solution.sortList(self.solution.create_single_linked_list([-4, 5, 2, 0, -1, -1, 5]))), [-4, -1, -1, 0, 2, 5, 5])
```
</blockquote></details>

```python
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


    def __str__(self):
        return '{} -> {}'.format(self.val, self.next)

class Solution:
    def sortList(self, head):
        if head == [] or head.next == None:
            return head
        return self.create_single_linked_list(self.merge_list(self.get_linked_list_values(head)))

    def merge_list(self, data):
        if len(data) < 2:
            return data

        left, right = data[: len(data) // 2], data[len(data) // 2:]
        left = self.merge_list(left)
        right = self.merge_list(right)

        index_left = index_right = 0
        result = []

        while index_left < len(left) and index_right < len(right):
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

        while index_left < len(left):
            result.append(left[index_left])
            index_left += 1

        while index_right < len(right):
            result.append(right[index_right])
            index_right += 1
        return result

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