from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s == ""):
            return True

        skimmed = ''.join(ch for ch in s if ch.isalnum()).lower()
        i, j = 0, len(skimmed) - 1

        while i < j:
            if skimmed[i] != skimmed[j]:
                return False
            i += 1
            j -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
