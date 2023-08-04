

# https://leetcode.com/problems/combination-sum/

from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, current, total):
            if total == target:
                result.append(current.copy())
                return

            if idx >= len(candidates) or total > target:
                return

            # left branch out
            current.append(candidates[idx])
            dfs(idx, current, total + candidates[idx])

            # cleanup
            current.pop()
            # right branch out
            dfs(idx+1, current, total)

        dfs(0, [], 0)
        return result


print(Solution().combinationSum([2, 3, 6, 7], 7))
