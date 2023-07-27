# https://leetcode.com/problems/reverse-linked-list/

from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    def recursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.recursively(head.next)
            head.next.next = head
        head.next = None
        return newHead

    def print(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next


# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1
five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)


# Solution().print(one)

# Solution().print(Solution().reverseList(one))

two = ListNode(2)
one = ListNode(1, two)
Solution().print(Solution().recursively(one))
