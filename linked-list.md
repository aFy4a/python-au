# Linked List

+ [Palindrome Linked List](#Palindrome_Linked_List)

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one_value(self):
        self.assertEqual(self.solution.isPalindrome(self.solution.create_single_linked_list([1])), 1)

    def test_odd_amount_true(self):
        self.assertEqual(self.solution.isPalindrome(self.solution.create_single_linked_list([1, 2, 3, 2, 1])), 1)

    def test_odd_amount_false(self):
        self.assertEqual(self.solution.isPalindrome(self.solution.create_single_linked_list([1, 2, 3, 2, 2])), 0)

    def test_even_amount_true(self):
        self.assertEqual(self.solution.isPalindrome(self.solution.create_single_linked_list([1, 2, 2, 1])), 1)

    def test_even_amount_false(self):
        self.assertEqual(self.solution.isPalindrome(self.solution.create_single_linked_list([1, 2, 2, 2])), 0)
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
    def isPalindrome(self, head):
        data = []
        while head != None:
            data.append(head.val)
            head = head.next

        check = 1
        for i in range(len(data) // 2):
            if (data[i] != data[len(data) - 1 - i]):
                check = 0
                break
        return check == 1

    def create_single_linked_list(self, values):
        if len(values) > 0:
            previous_node = ListNode(values[len(values)-1])
            for i in range(0, len(values) - 1):
                next_node = ListNode(values[len(values) - i - 2], previous_node)
                previous_node = next_node
            return previous_node
        else: return []
```