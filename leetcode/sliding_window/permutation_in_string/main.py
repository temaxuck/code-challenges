class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size, n = len(s1), len(s2)
        s1_sorted = sorted(s1)

        for end in range(window_size, n + 1):
            sub = sorted(s2[end - window_size : end])

            if s1_sorted == sub:
                return True

        return False


# print(Solution().checkInclusion("ab", "eidboaoo"))  # passed False
# print(Solution().checkInclusion("ab", "eidbaooo"))  # passed True
