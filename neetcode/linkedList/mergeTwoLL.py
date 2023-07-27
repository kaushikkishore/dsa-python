# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import *

# Definition for singly-linked list.
# both the linked lists are sorted in non decreseaing order


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

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

Solution().print(Solution().mergeTwoLists(l1_one, l2_one))

# result
# 1 -> 1 -> 2 -> 3 -> 4 -> 4
