# https://leetcode.com/problems/container-with-most-water/
from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while right > left:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1

        return maxArea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
