from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        nums.sort(reverse=True)
        nums_sum = sum(nums)
        if nums_sum % k:
            return False

        target_sum = sum(nums) // k
        sums = [0] * k

        def backtrack(idx):
            # idx - current index of element in `nums`
            if idx == n:
                return True

            for i in range(k):
                if sums[i] + nums[idx] <= target_sum:
                    sums[i] += nums[idx]

                    if backtrack(idx + 1):
                        return True

                    sums[i] -= nums[idx]

                    if sums[i] == 0:
                        return False

            return False

        return backtrack(0)


# print(
#     Solution().canPartitionKSubsets(
#         [
#             730,
#             580,
#             401,
#             659,
#             5524,
#             405,
#             1601,
#             3,
#             383,
#             4391,
#             4485,
#             1024,
#             1175,
#             1100,
#             2299,
#             3908,
#         ],
#         4,
#     )
# )

# print(Solution().canPartitionKSubsets([4, 16, 5, 3, 10, 4, 4, 4, 10], 3))
# print(Solution().canPartitionKSubsets([4, 4, 6, 2, 3, 8, 10, 2, 10, 7], 4))
# print(Solution().canPartitionKSubsets([1, 1, 1, 1, 2, 2, 2, 2], 2))
print(Solution().canPartitionKSubsets([1, 2, 3, 4], k=3))
