class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        current_s = ""

        for char in s:
            if char in current_s:
                max_length = max(max_length, len(current_s))
                for i in range(len(current_s)):
                    if current_s[i] == char:
                        current_s = current_s[i + 1 :] + char
                        break

            else:
                current_s += char

        max_length = max(max_length, len(current_s))

        return max_length


print(Solution().lengthOfLongestSubstring("dvdf"))  # passed 3
print(Solution().lengthOfLongestSubstring(" "))  # passed 1
print(Solution().lengthOfLongestSubstring("abcabcbb"))  # passed 3
