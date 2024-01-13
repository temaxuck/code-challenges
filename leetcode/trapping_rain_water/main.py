from typing import List
import heapq


class Solution:
    def top_two_values(self, l: List[int]):
        if len(l) < 2:
            return None
        first, second = (0, 1) if l[0] > l[1] else (1, 0)
        for i in range(2, len(l)):
            if l[i] > l[first]:
                first, second = i, first
            elif l[i] > l[second]:
                second = i
        return first, second

    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n < 3:
            return 0

        r, l = self.top_two_values(height)
        capacity = height[l] * (r - l - 1)

        for i in range(l + 1, r):
            capacity -= height[i]

        return (
            capacity
            + self.trap(height[: l + 1])
            + self.trap([v for v in reversed(height[r:])])
        )


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
