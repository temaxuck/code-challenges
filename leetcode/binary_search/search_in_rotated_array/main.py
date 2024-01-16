from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # If nums[l:m] is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # If nums[m:r] is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    """
    # My implementation:
    # Time Complexity: O(2logn) which is too much for leetcode
    
    def start_index(self, nums: List[int]) -> int:
        n = len(nums)
        start_index = 0
        l, r = 0, n - 1

        if n == 2:
            if nums[0] <= nums[1]:
                return 0
            else:
                return 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == nums[start_index]:
                break

            if nums[m] > nums[start_index]:
                l = m + 1
                continue

            if nums[m] < nums[start_index]:
                start_index = m
                r = m
                continue

        return start_index

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start_index = self.start_index(nums)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            actual_m = (start_index + m) % n  # actual m

            if target == nums[actual_m]:
                return actual_m

            if target > nums[actual_m]:
                l = m + 1
                continue

            if target < nums[m]:
                r = m - 1
                continue

        return -1
    """


print(Solution().search([2, 3, 4, 5, 1], 5))  # passed 11
# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))  # passed 11
