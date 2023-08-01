# https://leetcode.com/problems/binary-tree-right-side-view/
from typing import *
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        result = []

        while q:
            rightSide = None
            queLen = len(q)

            for i in range(queLen):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                result.append(rightSide.val)
        return result
