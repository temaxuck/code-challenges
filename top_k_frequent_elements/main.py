from typing import List


class Solution:

    """
    This is how I wanted to make solution, but couldn't write proper code

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heapq.heapify(nums)
        num_to_freq = {}
        while nums:
            smallest = heapq.heappop(nums)
            num_to_freq[smallest] = num_to_freq.get(smallest, 0) + 1

        output = []
        for i in range(k):
            mostFreq = max(num_to_freq, key=num_to_freq.get)
            del num_to_freq[mostFreq]
            output.append(mostFreq)
        return output

    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_order = {}

        for num in nums:
            nums_order[num] = nums_order.get(num, 0) + 1

        return [
            key
            for key, _ in sorted(nums_order.items(), key=lambda x: x[1], reverse=True)[
                :k
            ]
        ]

        # nums.sort()
        # print(nums)

        # top = [(0, 0)] * k
        # current_num = nums[0]
        # current_top = 0
        # for i in range(1, len(nums)):
        #     if nums[i] == current_num:
        #         top[]
        #     if len(nums) - i <= top[-1]:
        #         break


print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
