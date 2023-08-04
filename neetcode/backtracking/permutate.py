# https://leetcode.com/problems/permutations/
from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # copy the array.

        for i in range(len(nums)):
            n = nums.pop(0)

            # find all permutations like [1,2,3] 1 is removed here
            # remaining is [2,3] now we will get all combinations
            # [3,2] [2,3]
            perms = self.permute(nums)

            # for each of the returned perms you need to add the removed value
            for perm in perms:
                perm.append(n)

            # here we are adding multiple array to result array
            result.extend(perms)

            # add back the removed item
            nums.append(n)

        return result


print(Solution().permute([1, 2, 3]))
print(Solution().permute([1]))
