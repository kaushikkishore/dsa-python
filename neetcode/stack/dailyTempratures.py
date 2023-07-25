from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # this is a pair [temp, index]
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = (idx - stackIdx)
            stack.append([temp, idx])

        return result


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
