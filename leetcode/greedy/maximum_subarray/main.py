from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = float("-inf")

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum)

        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
