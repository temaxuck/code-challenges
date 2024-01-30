from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = float("-inf")
        cur_max_prod = nums[0]
        cur_min_prod = nums[0]

        for i in range(1, n):
            temp = cur_max_prod
            cur_max_prod = max(nums[i], cur_max_prod * nums[i], cur_min_prod * nums[i])
            cur_min_prod = min(nums[i], temp * nums[i], cur_min_prod * nums[i])
            max_prod = max(max_prod, cur_max_prod)

        return max_prod


# print(Solution().maxProduct([-2, -1, -3, -4]))
# print(Solution().maxProduct([-2, 0, -1, 0, 4, 3]))
# print(Solution().maxProduct([-2, 0, -1, 0]))
# print(Solution().maxProduct([0, 0, 3]))
# print(Solution().maxProduct([4, 3, 2, 1]))
# print(Solution().maxProduct([1, 2, 3, 4]))
# print(Solution().maxProduct([2, 3, -2, 4]))
