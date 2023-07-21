from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre = 1
        for idx, num in enumerate(nums):
            result[idx] = pre
            pre *= num

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))
