from typing import List
import heapq
from bisect import bisect_right


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.values = []

        for num in nums:
            self.values.bisect_right(num)
            if len(self.values) > k:
                assert False, "TODO: Implement MinHeap of k-length"

    def add(self, val: int) -> int:
        heapq.heappush(self.values, val)
        return heapq.nlargest(self.k, self.values)[-1]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
print(obj.add(4))
