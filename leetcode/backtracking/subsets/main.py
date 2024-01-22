from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []

        def backtrack(i):
            nonlocal res

            if i == n:
                res.append(path.copy())
                return

            backtrack(i + 1)

            path.append(nums[i])

            backtrack(i + 1)
            path.pop()

        backtrack(0)

        return res


print(Solution().subsets([1, 2, 3]))
