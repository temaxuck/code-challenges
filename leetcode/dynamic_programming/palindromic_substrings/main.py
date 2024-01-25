class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def helper(lc, rc):
            nonlocal res
            while 0 <= lc and rc < n and s[lc] == s[rc]:
                lc -= 1
                rc += 1
                res += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)

        return res


print(Solution().countSubstrings("cabad"))
