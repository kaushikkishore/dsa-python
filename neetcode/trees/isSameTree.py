# https://leetcode.com/problems/same-tree/

from typing import *
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if both are null then its same
        if not p and not q:
            return True

        # if one is null or values not matching then not equals
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
