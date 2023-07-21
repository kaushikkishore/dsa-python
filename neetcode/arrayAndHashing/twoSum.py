from typing import *
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for idx, num in enumerate(nums):
            itemToFind = target - num
            if itemToFind in myMap:
                return [idx, myMap[itemToFind]]

            myMap[num] = idx
