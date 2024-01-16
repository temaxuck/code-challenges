from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m

            if target > nums[m]:
                l = m + 1
                continue

            if target < nums[m]:
                r = m - 1
                continue

        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 23))
