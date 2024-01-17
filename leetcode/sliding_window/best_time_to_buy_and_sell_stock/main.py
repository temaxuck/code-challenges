from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(profit, max_profit)

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
