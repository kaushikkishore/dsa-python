# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitaToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backTrack(idx, currentString):
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            for c in digitaToChar[digits[idx]]:
                backTrack(idx+1, currentString+c)

        if digits:
            backTrack(0, "")
        return result


print(Solution().letterCombinations("23"))
