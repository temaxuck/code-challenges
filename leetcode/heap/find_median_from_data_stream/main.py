import heapq
from bisect import bisect_left


class MedianFinder:
    def __init__(self):
        self.data = []
        self.median = []
        self._median_gen = self._get_median()
        # next(self._median_gen)

    def _get_median(self):
        self.i = 0
        self.median.append(self.data[self.i])
        yield

        while True:
            self.i += 1
            self.median.append(self.data[self.i])
            yield
            self.median = self.median[1:]
            yield

    def addNum(self, num: int) -> None:
        self.i = bisect_left(self.data, num)
        print(self.i, self.data)
        self.data.insert(self.i, num)
        next(self._median_gen)

    def findMedian(self) -> float:
        return sum(self.median) / len(self.median)


def testcase_1():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1

    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5

    median_finder.addNum(3)
    assert median_finder.findMedian() == 2

    median_finder.addNum(4)
    assert median_finder.findMedian() == 2.5

    median_finder.addNum(5)
    assert median_finder.findMedian() == 3

    median_finder.addNum(3)
    assert median_finder.findMedian() == 3


testcase_1()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
