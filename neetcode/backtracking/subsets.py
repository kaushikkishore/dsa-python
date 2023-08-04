# https://leetcode.com/problems/subsets/
from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return

            # left side where the number is included
            subset.append(nums[idx])
            dfs(idx+1)

            # right side when the number is not included
            subset.pop()
            dfs(idx+1)

        # incoke the inner function
        dfs(0)

        # return the result now.
        return result


print(Solution().subsets([1, 2, 3]))
