from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutiveSet = set(nums)
        longest = 0

        for i in nums:
            # check if it is start of the sequence
            if (i - 1) not in consecutiveSet:
                length = 0
                while (i+length) in consecutiveSet:
                    length += 1

                longest = max(length, longest)
        return longest


Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
