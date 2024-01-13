from typing import List


class Solution:
    def binary_search(self, numbers: List[int], target: int, exclude: int) -> int:
        n = len(numbers)
        mid = n // 2
        l = 0
        r = n - 1

        while l <= r:
            if exclude == mid:
                l = mid + 1
                mid = (l + r) // 2
                continue
            if numbers[mid] == target:
                return mid
            if target > numbers[mid]:
                l = mid + 1
                mid = (l + r) // 2
                continue
            if target < numbers[mid]:
                r = mid - 1
                mid = (l + r) // 2
                continue

        return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            if (res := self.binary_search(numbers, target - numbers[i], i)) is not None:
                return [i + 1, res + 1]


print(Solution().twoSum([-2, -1, 0, 0], 0))
