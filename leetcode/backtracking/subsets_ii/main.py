from typing import List
from json import loads


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, cur):
            if i >= n:
                if not (to_add := sorted(cur[:])) in res:
                    res.append(to_add)
                return

            cur.append(nums[i])
            dfs(i + 1, cur)

            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])

        return res


print(Solution().subsetsWithDup([1, 2, 2]))
