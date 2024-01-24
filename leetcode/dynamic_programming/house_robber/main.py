from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        max_award = [0] * (n)
        max_award[0] = nums[0]
        max_award[1] = nums[1]
        max_award[2] = max(nums[1], nums[0] + nums[2])

        for i in range(3, n):
            max_award[i] = max(
                max_award[i - 1], max_award[i - 2] + nums[i], max_award[i - 3] + nums[i]
            )

        print(max_award)

        return max_award[-1]


# print(Solution().rob([2, 1, 1, 2]))

# passed
# print(Solution().rob([2, 7, 9, 3, 1]))

# passed
print(Solution().rob([1, 2, 3, 1]))
