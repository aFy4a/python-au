# Linked List

+ [Intersection of Two Linked Lists](#Intersection_of_Two_Linked_Lists)

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

<details><summary>Test case</summary><blockquote>

```python
import unittest
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cross(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sgetIntersectionNodes([1, 3, 4], self.solution.create_single_linked_list([1, 2, 3, 4]))), [3, 4])

    def test_two_cross(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sgetIntersectionNodes(self.solution.create_single_linked_list([4,1,8,4,5]), self.solution.create_single_linked_list([4,1,7,4,5]))), [4, 5])

    def test_nocross(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.sgetIntersectionNodes(self.solution.create_single_linked_list([1, 2, 3]), self.solution.create_single_linked_list([1, 3, 4]))), 0)
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
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        tempA = headA
        while tempA != None:
            lenA += 1
            tempA = tempA.next
        lenB = 0
        tempB = headB
        while tempB != None:
            lenB += 1
            tempB = tempB.next

        diff = abs(lenA - lenB)
        tempA = headA
        tempB = headB

        if lenA > lenB:
            while diff > 0:
                tempA = tempA.next
                diff -= 1
        else:
            while diff > 0:
                tempB = tempB.next
                diff -= 1

        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
            if tempA == None:
                return 0
        return tempA

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