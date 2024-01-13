import heapq
from typing import List


class Solution:
    def binary_search(self, sorted_nums, target, key=None):
        if key == None:
            key = lambda x: x

        low = 0
        high = len(sorted_nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = key(sorted_nums[mid])

            if guess == target:
                return sorted_nums[mid]
            elif guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        nums_w_indices = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(nums_w_indices)
        sorted_nums = [heapq.heappop(nums_w_indices) for _ in range(nums_len)]

        for i in range(nums_len):
            t = target - sorted_nums[i][0]
            if res := self.binary_search(sorted_nums[i + 1 :], t, key=lambda x: x[0]):
                return [sorted_nums[i][1], res[1]]


print(Solution().twoSum([-1, -2, -3, -4, -5], -8))
