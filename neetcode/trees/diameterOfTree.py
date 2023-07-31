# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            # daimeter of the treee for the node
            result[0] = max(result[0], 2 + left + right)

            return 1 + max(left, right)
        dfs(root)
        return result[0]
