# https://leetcode.com/problems/longest-repeating-character-replacement/
from typing import *


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0
        for right in range(len(s)):
            # increment the count of the char
            count[s[right]] = 1 + count.get(s[right], 0)

            # check the consition
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            result = max(right-left + 1, result)

        return result

    # more optimisation
    def characterReplacement2(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0
        maxFrequency = 0
        for right in range(len(s)):
            # increment the count of the char
            count[s[right]] = 1 + count.get(s[right], 0)

            maxFrequency = max(maxFrequency, count[s[right]])

            # check the consition
            while (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1

            result = max(right-left + 1, result)

        return result


print(Solution().characterReplacement2("ABAB", 2))
print(Solution().characterReplacement2("AABABBA", 1))

print(Solution().characterReplacement2("ABAA", 0))
