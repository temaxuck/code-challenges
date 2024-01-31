from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        max_seq = 1

        for i in range(1, n):
            j = i - 1
            cur_max_seq = 0
            while j >= 0:
                if nums[i] > nums[j]:
                    cur_max_seq = max(cur_max_seq, dp[j])
                j -= 1
            dp[i] += cur_max_seq
            max_seq = max(max_seq, dp[i])

        return max_seq


print(Solution().lengthOfLIS([0]))
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
