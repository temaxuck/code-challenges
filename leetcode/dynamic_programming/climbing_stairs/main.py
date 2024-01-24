class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1

        table = [1] * (n + 1)

        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]

        return table[-1]


print(Solution().climbStairs(44))
