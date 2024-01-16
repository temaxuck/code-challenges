from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        v = nums[0]
        l, r = 0, n - 1

        if n == 2:
            return min(nums)

        while l <= r:
            m = l + (r - l) // 2

            # print(l, m, r, nums[m], v)
            # input()

            if nums[m] == v:
                return v

            if nums[m] > v:
                l = m + 1
                continue

            if nums[m] < v:
                v = nums[m]
                r = m
                continue

        return v


print(Solution().findMin([2, 3, 1]))  # passed 1
print(Solution().findMin([1]))  # passed 1
print(Solution().findMin([1, 2]))  # passed 1
print(Solution().findMin([3, 4, 5, 1, 2]))  # passed 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # passed 0
print(Solution().findMin([11, 13, 15, 17]))  # passed 11
