# https://leetcode.com/problems/word-search/
from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                    (r, c) in path):
                return False

            path.add((r, c))

            result = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            path.remove((r, c))
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

# O(n * m * 4^n) - first n is rows , m is colms , 4 means for direction dfs call
# n is number of words


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]], "ABCCED"))

print(Solution().exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
print(Solution().exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
