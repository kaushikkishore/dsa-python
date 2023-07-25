# https://leetcode.com/problems/valid-parentheses/
from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {"}": "{", "]": "[", ")": "("}
        stack = []

        for char in s:
            if char in charMap:
                if stack and stack[-1] == charMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


print(Solution().isValid("()[]{}"))

print(Solution().isValid("([)]{}"))
