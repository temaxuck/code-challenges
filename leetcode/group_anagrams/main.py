from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_strs = {}
        for i, str in enumerate(strs):
            # a better solution would be to calculate sum of hashes for each char
            # key = sum([hash(c) for c in str])

            # my solution
            key = tuple(sorted([ord(c) for c in str]))
            ord_strs[key] = (ord_strs.get(key) or []) + [str]

        return [value for value in ord_strs.values()]


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
