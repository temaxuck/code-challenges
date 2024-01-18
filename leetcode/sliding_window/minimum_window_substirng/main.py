class Solution:
    def contains(self, d):
        return all([True if v < 1 else False for v in d.values()])

    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        min_window = ""

        if n > m:
            return min_window

        d = {}
        start, end = 0, 0

        for c in t:
            d[c] = d.get(c, 0) + 1

        while end < m:
            if s[end] in d:
                d[s[end]] -= 1

            while self.contains(d) and start <= end:
                min_window = (
                    s[start : end + 1]
                    if min_window == "" or len(s[start : end + 1]) < len(min_window)
                    else min_window
                )

                if s[start] in d:
                    d[s[start]] += 1

                start += 1

            end += 1

        return min_window


print(Solution().minWindow("a", "a"))  # PASSED a
print(Solution().minWindow("ADOBECODEBANC", "ABC"))  # PASSED BANC
