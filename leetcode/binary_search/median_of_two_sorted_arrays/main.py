from typing import List
from bisect import insort_right


class Solution:
    def binary_search(self, nums: List[int], target: int):
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
                continue

            if target <= nums[m]:
                r = m
                continue

        return l

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        l, r = 0, n - 1
        result_list = nums1[:]

        for num in nums2:
            insort_right(result_list, num)

        if (n + m) % 2:
            return result_list[(n + m) // 2]
        else:
            return (result_list[(n + m) // 2] + result_list[(n + m) // 2 - 1]) / 2


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))  # passed 11
print(Solution().findMedianSortedArrays([1, 3], [2]))  # passed 11
