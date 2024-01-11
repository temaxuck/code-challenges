class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        s_letters = [0] * 26
        t_letters = [0] * 26

        for i in range(s_len):
            s_letters[ord(s[i]) - 97] += 1
            t_letters[ord(t[i]) - 97] += 1

        return s_letters == t_letters
