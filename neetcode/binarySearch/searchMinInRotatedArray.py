# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        value = nums[0]
        while right >= left:
            if nums[left] < nums[right]:
                # found the min here already break now
                value = min(value, nums[left])
                break

            mid = (left + right) // 2
            value = min(value, nums[mid])

            if nums[mid] >= nums[left]:
                # search right
                left = mid + 1
            else:
                # search left
                right = mid - 1

        return value


print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
