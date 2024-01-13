from typing import List
import heapq


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        l, r = 0, n - 1
        max_l, max_r = height[l], height[r]
        capacity = 0

        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

            if max_l < max_r:
                capacity += max_l - height[l]
                l += 1
            else:
                capacity += max_r - height[r]
                r -= 1

        return capacity


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
