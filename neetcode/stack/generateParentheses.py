from typing import *
# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Will obly add open paranthesis if open < n
        # only add close paranthesis if closed < open
        # valid if open == close == n

        stack = []
        result = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                return result.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()

        backtrack(0, 0)

        return result


# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(3))
