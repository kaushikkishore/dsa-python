from typing import *
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        first = {}
        second = {}

        for _, char in enumerate(s):
            first[char] = 1 + first.get(char, 0)

        for _, char in enumerate(t):
            second[char] = 1 + second.get(char, 0)

        for key in first:
            if first[key] != second.get(key, 0):
                return False

        return True


assert Solution().isAnagram("anagram", "nagaram") == True, "Failed case"
assert Solution().isAnagram("rat", "car") == False, "Failed case"
