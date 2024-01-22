from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        def dfs(i, cur):
            nonlocal res

            cur_sum = sum(cur)

            if cur_sum == target:
                res.append(cur.copy())
                return

            if cur_sum > target:
                return

            if i >= n:
                return

            cur.append(candidates[i])
            dfs(i, cur)

            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])

        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
