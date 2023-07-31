# https://leetcode.com/problems/reorder-list/

from typing import *

# Definition for singly-linked list.
# both the linked lists are sorted in non decreseaing order


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # noe need to reverse the rest of the list of the slow pointer
        # reverse the teamp LL
        second = slow.next

        # split the slow list
        slow.next = None

        # reverse process
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two halfs of the list
        # bening of the secons is prev
        first, second = head, prev

        # second will be shorter
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            # shift points
            first, second = temp1, temp2

    def print(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next


# 1 -> 2 -> 4
four = ListNode(4, None)
two = ListNode(2, four)
l1_one = ListNode(1, two)


# 1 -> 3 -> 4 -> 7 -> 9 -> 11
eleven = ListNode(11, None)
nine = ListNode(9, eleven)
seven = ListNode(7, nine)
l2_four = ListNode(4, seven)
three = ListNode(3, l2_four)
l2_one = ListNode(1, three)

# Solution().print(Solution().mergeTwoLists(l1_one, l2_one))

# result
# 1 -> 1 -> 2 -> 3 -> 4 -> 4
