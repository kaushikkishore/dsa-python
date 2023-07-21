from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uq = set()
        for num in nums:
            if num in uq:
                return True
            uq.add(num)

        return False
