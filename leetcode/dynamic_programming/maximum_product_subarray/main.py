from typing import List
from functools import reduce


class Solution:
    def kron_delta(self, condition):
        if condition:
            return 1

        return 0

    def product_of_slice(self, slice):
        return reduce(lambda x, y: x * y, slice)

    def product_of_slice_odd_neg(self, slice):
        prod1, prod2 = 1, 1

        for i in range(len(slice)):
            ...

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        negative_cnt = 0
        partitions = []
        max_prod = float("-inf")
        i, prev_i = 0, 0

        while True:
            negative_cnt += self.kron_delta(nums[i] < 0)
            if self.kron_delta(nums[i] == 0):
                partitions.append((prev_i, i, negative_cnt))
                negative_cnt = 0
                prev_i = i + 1
            i += 1
            if i >= n:
                partitions.append((prev_i, i, negative_cnt))
                prev_i = i
                break

        for partition in partitions:
            start, stop, neg = partition
            slice = nums[start:stop]

            if slice:
                if neg % 2:
                    max_prod = max(
                        self.product_of_slice(slice),
                        max_prod,
                    )

        # for i in range(1, n):
        #     dp[i] = max(dp[i], dp[i - 1] * dp[i])

        # def helper(index, current_prod):
        #     print(index, current_prod)
        #     nonlocal max_prod

        #     if index >= n:
        #         return

        #     if current_prod is None:
        #         current_prod = nums[index]
        #     else:
        #         current_prod *= nums[index]

        #     max_prod = max(current_prod, max_prod)

        #     helper(index + 1, current_prod)
        #     helper(index + 1, None)

        # helper(0, None)

        # return max_prod


# print(Solution().maxProduct([-2, -1, -3, -4]))
# print(Solution().maxProduct([-2, 0, -1, 0, 4, 3]))
print(Solution().maxProduct([-2, 0, -1, 0]))
# print(Solution().maxProduct([4, 3, 2, 1]))
# print(Solution().maxProduct([1, 2, 3, 4]))
# print(Solution().maxProduct([2, 3, -2, 4]))
