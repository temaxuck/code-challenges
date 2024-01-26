class Solution:
    VALID_RANGE = range(1, 27)
    MAX_VALID_TOKEN_LENGTH = len(str(VALID_RANGE.stop - 1))

    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {n: 1}

        def helper(i):
            if i in cache:
                return cache[i]

            if s[i] == "0":
                return 0

            res = helper(i + 1)

            if i + 1 < n and int(s[i : i + 2]) in self.VALID_RANGE:
                res += helper(i + 2)

            cache[i] = res
            return res or 0

        return helper(0)


print(Solution().numDecodings("10"))
