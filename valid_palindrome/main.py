import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        s_len = len(s)

        for i in range(s_len // 2):
            j = s_len - i - 1

            if s[i] != s[j]:
                return False

        return True


print(Solution().isPalindrome("ab_a"))
