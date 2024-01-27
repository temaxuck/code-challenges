from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [*[0], *[float("inf")] * amount]

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(1 + dp[i - coin], dp[i])

        if dp[-1] == float("inf"):
            return -1

        return dp[-1]


print(Solution().coinChange([5, 306, 188, 467, 494], 7047))
print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([186, 419, 83, 408], 6249))
print(Solution().coinChange([3, 7, 405, 436], 8839))
