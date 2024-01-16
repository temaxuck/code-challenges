from typing import List


class Solution:
    def area(self, w, h):
        return w * h

    # Efficient solution
    # Time complexity: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        i = 0

        while i < len(heights):
            if (not stack) or (heights[stack[-1]] <= heights[i]):
                stack.append(i)
                i += 1
            else:
                curr_height = heights[stack.pop()]  # current min height
                max_area = max(
                    max_area,
                    self.area((i - stack[-1] - 1) if stack else i, curr_height),
                )
            print([heights[i] for i in stack], max_area)

        while stack:
            curr_height = heights[stack.pop()]  # current min height
            max_area = max(
                max_area, self.area((i - stack[-1] - 1) if stack else i, curr_height)
            )
            print([heights[i] for i in stack], max_area)

        return max_area

    """
    def min_index(self, l: List[int], range_obj=None) -> (int, int):
        if not range_obj:
            range_obj = range(0, len(l))
        res = (l[0], 0)
        i, j = range_obj.start, range_obj.stop - 1

        while i <= j:
            if l[i] < res[0]:
                res = (l[i], i)
            if l[j] < res[0]:
                res = (l[j], j)

            i += 1
            j -= 1

        return res
        
    # Inefficient solution: 
    # Time: O(n^2)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [heights]

        while stack:
            curr_heights = stack.pop()

            if not curr_heights:
                continue


            val, idx = self.min_index(curr_heights)

            if (curr_area := self.area(len(curr_heights), val)) > max_area:
                max_area = curr_area

            stack.append(curr_heights[:idx])
            stack.append(curr_heights[idx + 1 :])
            print(stack, curr_heights, val, idx)

        return max_area
    """


print(Solution().largestRectangleArea([2, 0, 2]))
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # passed 10
