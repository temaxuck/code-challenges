from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("(", 1, 0)]

        while stack:
            s, opened, closed = stack.pop()

            if opened - closed < 0:
                continue

            if opened == closed == n:
                res.append(s)
                continue

            if closed < opened:
                stack.append((s + ")", opened, closed + 1))
            if opened < n:
                stack.append((s + "(", opened + 1, closed))

        return res


print(Solution().generateParenthesis(3))
