from typing import List


class Solution:
    def area(self, width, height):
        return width * height

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        max_area = -1

        while l < r:
            if (area := self.area(r - l, min(height[l], height[r]))) > max_area:
                max_area = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
