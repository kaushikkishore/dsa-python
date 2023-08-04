# https://leetcode.com/problems/combination-sum-ii/

from typing import *

# time complexity O(n * 2^n)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # sort the candidates
        candidates.sort()

        def backtrack(idx, current, total):
            if total == target:
                result.append(current[::])
                return

            if idx >= len(candidates) or total > target:
                return

            # left branch
            current.append(candidates[idx])
            backtrack(idx+1, current, total+candidates[idx])

            # remove item now
            current.pop()

            # right branch out
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1

            # backtrack again
            backtrack(idx+1, current, total)

        backtrack(0, [], 0)
        return result

    def combinationSumWay2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def backtrack(current, idx, target):
            if target == 0:
                result.append(current[::])

            # this means we finished the loop or target is nore than given amount
            if target <= 0:
                return

            prev = -1

            # iterate the candidates from specified place
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue

                # left branch out
                current.append(candidates[i])
                backtrack(current, i+1, target - candidates[i])

                # pop out the element
                current.pop()

                # so we can determine when to skip this process.
                prev = candidates[i]

        backtrack([], 0, target)
        return result


print(Solution().combinationSumWay2([10, 1, 2, 7, 6, 1, 5], 8))
