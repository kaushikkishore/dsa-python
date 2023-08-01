# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    def inOrder(self, root: Optional[TreeNode]) -> None:
        if root:
            self.inOrder(root.left)

            print(root.val, end=" ")

            self.inOrder(root.right)


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

result = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

Solution().inOrder(result)
