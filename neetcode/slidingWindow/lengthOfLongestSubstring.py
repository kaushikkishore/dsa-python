# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        left = 0

        maxLength = 0

        for idx in range(len(s)):
            while s[idx] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[idx])
            maxLength = max(maxLength, idx - left + 1)
        return maxLength


print(Solution().lengthOfLongestSubstring("abcabcbb"))
