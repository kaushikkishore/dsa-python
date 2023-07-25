from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                sec = stack.pop()
                first = stack.pop()
                result = first + sec
                stack.append(result)

            elif t == "-":
                sec = stack.pop()
                first = stack.pop()
                result = first - sec
                stack.append(result)

            elif t == "*":
                sec = stack.pop()
                first = stack.pop()
                result = first * sec
                stack.append(result)

            elif t == "/":
                sec = stack.pop()
                first = stack.pop()
                result = int(first / sec)
                stack.append(result)

            else:
                stack.append(int(t))

        return stack[-1]


# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
print(Solution().evalRPN(["2", "1", "-", "3", "/"]))
