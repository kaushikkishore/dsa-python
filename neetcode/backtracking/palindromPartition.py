# https://leetcode.com/problems/palindrome-partitioning/

from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        partition = []

        def dfs(idx):
            if idx >= len(s):
                result.append(partition.copy())
                return

            for j in range(idx, len(s)):
                if self.isPlandrom(s, idx, j):
                    partition.append(s[idx:j+1])
                    dfs(j+1)
                    partition.pop()

        dfs(0)
        return result

    def isPlandrom(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1

        return True


print(Solution().partition("aab"))
