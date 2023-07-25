# https://leetcode.com/problems/koko-eating-bananas/


from typing import *
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        result = maxSpeed

        left, right = 1, maxSpeed

        while right >= left:
            mid = (left + right) // 2
            hoursToEatAll = 0
            for pile in piles:
                hoursToEatAll += math.ceil(pile/mid)

            if hoursToEatAll > h:
                left = mid + 1
            elif hoursToEatAll <= h:
                result = min(result, mid)
                right = mid - 1

        return result


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
