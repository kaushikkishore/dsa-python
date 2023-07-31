# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import *

# Definition for singly-linked list.
# both the linked lists are sorted in non decreseaing order


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left, right = dummy, head

        # create a n distance between left and right
        while n > 0 and right:
            right = right.next
            n -= 1

        # now move the points till right reaches the None
        while right:
            right = right.next
            left = left.next

        # now the left will on the position where we need to remove the node
        # delete the item
        left.next = left.next.next

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

# Solution().print(Solution().mergeTwoLists(l1_one, l2_one))

# result
# 1 -> 1 -> 2 -> 3 -> 4 -> 4
