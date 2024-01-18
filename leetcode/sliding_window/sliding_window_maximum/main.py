from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums[0]

        res = []
        dq = deque()

        for r in range(0, n):
            while dq and nums[r] > dq[-1][0]:
                dq.pop()
            dq.append((nums[r], r))
            if r >= k - 1:
                if dq[0][1] < r - k + 1:
                    dq.popleft()
                res.append(dq[0][0])

        return res

    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        min_el = nums[0]
        res = []
        dq = deque()
        dq.append((min_el, 0))

        for r in range(1, n):
            while dq and nums[r] < dq[-1][0]:
                dq.pop()
            dq.append((nums[r], r))
            if r >= k - 1:
                if dq[0][1] < r - k + 1:
                    dq.popleft()
                res.append(dq[0][0])

        return res


print(Solution().maxSlidingWindow([1, -1], 1))  # PASSED
# print(Solution().minSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # PASSED
# print(Solution().minSlidingWindow([2, 1, 4, 5, 3, 4, 1, 2], 4))  # PASSED
# print(Solution().maxSlidingWindow([1, 2, 3, 7, 5, 6, 7, 8], 3))  # PASSED
# print(Solution().maxSlidingWindow([5, 4, 3, 2, 1], 3))  # PASSED
# print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # PASSED
