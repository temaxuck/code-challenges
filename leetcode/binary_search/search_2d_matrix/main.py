from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return True

            if target > nums[m]:
                l = m + 1
                continue

            if target < nums[m]:
                r = m - 1
                continue

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        t, b = 0, rows - 1

        while t <= b:
            m = t + (b - t) // 2

            if matrix[m][-1] == target:
                return True

            if target > matrix[m][-1]:
                t = m + 1
                continue

            if target < matrix[m][-1]:
                if target >= matrix[m][0]:
                    if target == matrix[m][0]:
                        return True

                    return self.binary_search(matrix[m], target)

                b = m - 1
                continue

        return False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
