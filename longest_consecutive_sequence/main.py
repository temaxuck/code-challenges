from typing import List
import heapq


class Solution:
    def longest_sequence(
        self, heap, heap_size, prev_num, current_sequence, longest_sequence
    ):
        if current_sequence > longest_sequence:
            longest_sequence = current_sequence

        l, r = 1, 2
        if l < heap_size and heap[l] == prev_num + 1:
            prev_num = heap[l]
            heapq.heappop(heap)
            longest_sequence = self.longest_sequence(
                heap, heap_size - 1, prev_num, current_sequence + 1, longest_sequence
            )
        elif r < heap_size and heap[r] == prev_num + 1:
            prev_num = heap[r]
            heapq.heappop(heap)
            longest_sequence = self.longest_sequence(
                heap, heap_size - 1, prev_num, current_sequence + 1, longest_sequence
            )
        elif 1 < heap_size:
            heapq.heappop(heap)
            longest_sequence = self.longest_sequence(
                heap, heap_size - 1, heap[0], 1, longest_sequence
            )

        return longest_sequence

    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        heap_size = len(unique_nums)

        if heap_size == 0:
            return 0

        heapq.heapify(unique_nums)
        return self.longest_sequence(unique_nums, heap_size, unique_nums[0], 1, 0)


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
