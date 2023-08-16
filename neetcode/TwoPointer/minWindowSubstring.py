# https://leetcode.com/problems/minimum-window-substring/
from typing import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}

        for targetC in t:
            countT[targetC] = 1 + countT.get(targetC, 0)

        # define have and need
        have, need = 0, len(countT)

        # for result purpose
        result, resultLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1) < resultLen:
                    result = [l, r]
                    resultLen = (r-l + 1)
                # pop from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l: r+1] if resultLen != float("infinity") else ""

    def minWindow2(self, s: str, t: str) -> str:
        #
        if len(t) > len(s):
            return ""

        if s == t:
            return s

        haveMap, targetMap = {}, {}
        minString = s[::]
        left, right = 0, 0
        # have and target map setup done
        for item in t:
            if item not in targetMap:
                targetMap[item] = 0
            targetMap[item] += 1
            haveMap[item] = 0
        #
        while right < len(s):
            rightChar = s[right]
            if rightChar in targetMap:
                haveMap[rightChar] += 1
                while self.isMapsEqual(haveMap, targetMap):
                    newString = s[left:right+1]
                    if len(newString) < len(minString):
                        minString = newString
                    # move head the left pointer untill the both maps are not equal

                    if s[left] in haveMap:
                        haveMap[s[left]] -= 1
                    left += 1

            right += 1
        return "" if s == minString else minString
        # check if the have map is euqal to target map

    def isMapsEqual(self, have, target):
        for t in target:
            if have[t] < target[t]:
                return False
        return True


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
