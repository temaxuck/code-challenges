from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 4:
            return max(nums)

        prev1, next1 = 0, nums[0]
        prev2, next2 = 0, nums[1]

        for i in range(1, n - 1):
            next1, prev1 = max(prev1 + nums[i], next1), next1
            next2, prev2 = max(prev2 + nums[i + 1], next2), next2

        return max(next1, next2)


# print(Solution().rob([2, 7, 9, 3, 1]))
# print(Solution().rob([1, 7, 9, 4]))
# print(Solution().rob([1, 7, 9, 2]))
# print(Solution().rob([200, 3, 140, 20, 10]))
# print(Solution().rob([1, 2, 1, 1]))
# Pass
# print(Solution().rob([1, 2, 3, 1]))
