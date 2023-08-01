from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, root: Optional[TreeNode]) -> None:
        if root:
            self.inOrder(root.left)

            print(root.val, end=" ")

            self.inOrder(root.right)

    def preOrder(self, root: Optional[TreeNode]) -> None:
        if root:
            print(root.val, end=" ")

            self.preOrder(root.left)

            self.preOrder(root.right)

    def postOrder(self, root: Optional[TreeNode]) -> None:
        if root:

            self.postOrder(root.left)

            self.postOrder(root.right)

            print(root.val, end=" ")


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

print("Inorder traversal")
Solution().inOrder(five)
print()

print("Pre Order traversal")
Solution().preOrder(five)
print()

print("Post order traversal")
Solution().postOrder(five)
