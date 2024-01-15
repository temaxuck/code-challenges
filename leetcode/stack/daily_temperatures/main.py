from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        My idea would be to sort temperatures with heap sort
        preserving indexes of each element, and to fill result
        list with proper values.

        But since I'm trainig stack, this solution is present.
        """
        n = len(temperatures)
        res = [0] * n
        stack = [(temperatures[0], 0)]

        for i in range(1, n):
            curr = temperatures[i]

            while stack:
                prev_t, prev_i = stack[-1]

                if curr > prev_t:
                    res[prev_i] = i - prev_i
                    stack.pop()
                else:
                    break

            stack.append((curr, i))

        return res


print(Solution().dailyTemperatures([90, 80, 70]))
