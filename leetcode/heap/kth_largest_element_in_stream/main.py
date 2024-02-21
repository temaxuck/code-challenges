from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.values = []

        for num in nums:
            if len(self.values) < k:
                heapq.heappush(self.values, num)
            else:
                heapq.heappushpop(self.values, num)

    def add(self, val: int) -> int:
        if len(self.values) < self.k:
            heapq.heappush(self.values, val)
        else:
            heapq.heappushpop(self.values, val)
        return self.values[0]


obj = KthLargest(1, [])
print(obj.values)
print(obj.add(-3))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(0))
print(obj.add(4))


# Passed
# obj = KthLargest(3, [4, 5, 8, 2])
# print(obj.values)
# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))
# print(obj.add(4))
