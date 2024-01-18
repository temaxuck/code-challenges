class Solution:
    def most_popular(self, count: dict):
        return max(count.items(), key=lambda x: x[1])

    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0

        count = {}  # within window
        start, end = 0, 0  # window constraints
        moved = True

        while end < n:
            if moved:
                count[s[end]] = count.get(s[end], 0) + 1

            # check if we should expand or shrink window
            if (end - start + 1) - self.most_popular(count)[1] > k:
                count[s[start]] -= 1
                start += 1
                moved = False
            else:
                max_length = max(end - start + 1, max_length)
                # update count
                end += 1
                moved = True

        return max_length


print(Solution().characterReplacement("ABBB", 2))  # passed 4
print(Solution().characterReplacement("AABABBA", 1))  # passed 4
print(Solution().characterReplacement("ABAB", 2))  # passed 4
