# https://leetcode.com/problems/binary-search/
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while end >= start:
            mid = (end + start) // 2
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1

        return -1


# print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
