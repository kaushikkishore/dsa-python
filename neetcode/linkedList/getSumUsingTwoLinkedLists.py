# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# edge cases
# 7 + 8 = 15
# when one ll ends but other is there
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        carry = 0
        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # new digit
            val = val1 + val2 + carry

            carry = val // 10
            val = val % 10

            current.next = ListNode(val)

            # update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# 1 -> 2 -> 4
four = ListNode(4, None)
two = ListNode(2, four)
one = ListNode(1, two)


# 7 -> 9 -> 1
eleven = ListNode(1, None)
nine = ListNode(9, eleven)
seven = ListNode(7, nine)

# 197 + 421 = 618


Solution().addTwoNumbers(one, seven)
