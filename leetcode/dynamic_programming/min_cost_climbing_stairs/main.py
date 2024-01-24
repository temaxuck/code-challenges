from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = [*[0], *cost]
        n = len(cost)
        min_cost = [0] * n
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, n):
            min_cost[i] = min(min_cost[i - 1], min_cost[i - 2]) + cost[i]
        return min(min_cost[-2:])


# passed
print(Solution().minCostClimbingStairs([0, 2, 2, 1]))
# Passed
# print(Solution().minCostClimbingStairs([10, 15, 20]))
# Passed
# print(Solution().minCostClimbingStairs([1, 100, 1000, 100]))
