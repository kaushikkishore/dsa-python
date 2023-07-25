# https://leetcode.com/problems/search-a-2d-matrix/
from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        print(ROWS, COLS)

        # find the row first where the numer belongs to.
        top, bottom = 0, ROWS - 1

        # find the middle row
        while bottom >= top:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow-1
            else:
                break

        print(midRow, top, bottom)

        if not (top <= bottom):
            return False

        row = (top+bottom) // 2
        left, right = 0, COLS - 1

        while right >= left:
            mid = (left + right) // 2

            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
