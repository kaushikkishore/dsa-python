# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right >= left:

            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                # means middle is left sorted portion
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # means middle is in right sorted portion
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
