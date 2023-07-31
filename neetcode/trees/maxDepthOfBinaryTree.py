# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative
    def bfs(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # que wil have root and then add item in queue
        level = 0

        queue = deque([root])
        while queue:

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def dfsIterative(self,  root: Optional[TreeNode]) -> int:

        # use the stack
        # pre order DFS
        stack = [[root, 1]]
        result = 0
        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result
