# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative solution
        n = 0
        stack = [root]
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            n += 1

            if k == n:
                return curr.val

            curr = curr.right


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
five = TreeNode(5)
three = TreeNode(3)
six = TreeNode(6)
two = TreeNode(2)
four = TreeNode(4)
one = TreeNode(1)

five.left = three
five.right = six

three.left = two
three.right = four

two.left = one


print(Solution().kthSmallest(five, 3))
