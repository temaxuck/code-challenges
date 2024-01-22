from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(pool, cur):
            if len(cur) >= n:
                res.append(cur.copy())
                return

            for i, num in enumerate(pool):
                cur.append(num)
                dfs([*pool[:i], *pool[i + 1 :]], cur)
                cur.pop()

        dfs(nums, [])

        return res


print(Solution().permute([1, 2, 3]))
