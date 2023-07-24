# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while (j > i):
            currentSum = numbers[i] + numbers[j]
            if (currentSum > target):
                j -= 1
            elif currentSum < target:
                i += 1
            elif currentSum == target:
                return [i+1, j+1]

        return [-1, -1]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 3, 4], 6))
print(Solution().twoSum([-1, 0], -1))
