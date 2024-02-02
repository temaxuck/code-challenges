from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        distances = []

        for point in points:
            x, y = point
            heapq.heappush(distances, (-(x * x + y * y), [x, y]))
            if len(distances) > k:
                heapq.heappop(distances)

        return [heapq.heappop(distances)[1] for _ in range(k)]


print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
# print(Solution().kClosest([[1, 3], [-2, 2]], 1))
