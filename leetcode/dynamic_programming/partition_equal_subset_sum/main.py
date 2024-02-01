from typing import List


class Solution:
    PARTITIONS_NUM = 2

    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        nums_sum = sum(nums)

        if nums_sum % self.PARTITIONS_NUM:
            return False

        target_sum = nums_sum // self.PARTITIONS_NUM
        sums = [0] * self.PARTITIONS_NUM
        cache = {}

        def backtrack(idx):
            # idx - current index of element in `nums`
            if (idx, str(sums)) in cache:
                return cache[(idx, str(sums))]

            if idx == n:
                cache[(idx, str(sums))] = True
                return True

            for i in range(self.PARTITIONS_NUM):
                if sums[i] + nums[idx] <= target_sum:
                    sums[i] += nums[idx]

                    if backtrack(idx + 1):
                        cache[(idx, str(sums))] = True
                        return True

                    sums[i] -= nums[idx]

                    if sums[i] == 0:
                        cache[(idx, str(sums))] = False
                        return False

            cache[(idx, str(sums))] = False
            return False

        return backtrack(0)


print(
    Solution().canPartition(
        [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            99,
            97,
        ]
    )
)
print(Solution().canPartition([1, 5, 11, 5]))
