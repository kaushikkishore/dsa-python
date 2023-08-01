# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
from collections import deque
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS Level order traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            qLen = len(queue)
            level = []
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)

        return result
