# https://leetcode.com/problems/subsets-ii/
from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort the nums so that we can move the points in case of duplicates
        nums.sort()

        def backtrack(idx, subset):
            # base case where the index is equal to the nums list
            if idx == len(nums):
                result.append(subset[::])
                return

            # left subtree when we are going to include the char
            subset.append(nums[idx])
            backtrack(idx+1, subset)

            # remove the item as we are done backtracking
            subset.pop()

            # right when we are not including
            # when we are not including in that case we need to move pointers forwards
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1

            # invoke the backtrack now again
            backtrack(idx+1, subset)

        backtrack(0, [])
        return result


print(Solution().subsetsWithDup([1, 3, 2, 2]))
