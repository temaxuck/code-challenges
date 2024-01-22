from typing import List
from collections import defaultdict, Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        d = defaultdict(int)
        res = []

        for candidate in candidates:
            d[candidate] += 1

        def dfs(t, cur, counter):
            if t == 0:
                res.append(cur)
                return

            if t < 0:
                return

            for candidate in counter:
                if counter[candidate] > 0 and t - candidate >= 0:
                    counter_copy = counter.copy()
                    counter[candidate] = 0
                    counter_copy[candidate] -= 1
                    dfs(t - candidate, [*cur, *[candidate]], counter_copy)

        dfs(target, [], d)

        return res


print(
    Solution().combinationSum2(
        [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            33,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            44,
            4,
            4,
            4,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            49,
            5,
            5,
            5,
            5,
            6,
            6,
            6,
            6,
        ],
        29,
    )
)
# print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
