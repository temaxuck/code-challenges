from typing import List
from collections import defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)

        max_freq = 0
        tasks_with_max_freq = 0

        for task in tasks:
            freq[task] += 1
            max_freq = max(max_freq, freq[task])

        for freq_v in freq.values():
            tasks_with_max_freq += int(freq_v == max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + tasks_with_max_freq)


print(Solution().leastInterval([""], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
