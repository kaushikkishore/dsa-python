# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,  1  # left = buy, right = sell
        maxProfit = 0
        while right < len(prices):
            buyPrice = prices[left]
            sellPrice = prices[right]

            if buyPrice < sellPrice:
                profit = sellPrice - buyPrice
                maxProfit = max(sellPrice - buyPrice, maxProfit)
            else:
                left = right
            right += 1

        return maxProfit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


print(Solution().maxProfit([7, 6, 4, 3, 1]))
