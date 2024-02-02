from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]

        pop, push = heapq.heappop, heapq.heappush
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = pop(stones), pop(stones)

            if y == x:
                continue

            push(stones, x - y)

        return 0 if not stones else -stones[0]


print(Solution().lastStoneWeight([3, 7, 2]))
print(Solution().lastStoneWeight([1, 3]))
print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
