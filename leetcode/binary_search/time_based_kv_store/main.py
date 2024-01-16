class TimeMap:
    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # store values as list of tuples sorted (value, timestamp)
        if self.hash_map.get(key) is None:
            self.hash_map[key] = [(value, timestamp)]
        else:
            self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # get either the value at timestamp `timestamp`
        # or if not found value to the left of next

        if self.hash_map.get(key) is None or self.hash_map[key][1] > timestamp:
            return ""

        n = len(self.hash_map[key])
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            v, t = self.hash_map[key][m]

            if timestamp == t:
                return self.hash_map[key][m][0]

            if timestamp > t:
                l = m + 1
                continue
            else:
                r = m
                continue

        return self.hash_map[key][l - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set("foo", "bar", 1)
# obj.get("foo", 1)
# obj.get("foo", 3)
# obj.set("foo", "bar2", 4)
# obj.get("foo", 4)
# obj.get("foo", 5)
obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
print(obj.get("love", 5))
print(obj.get("love", 10))
print(obj.get("love", 15))
print(obj.get("love", 20))
print(obj.get("love", 25))
# print(obj.hash_map)
# obj.get("foo", 3)
# obj.set("foo", "bar2", 4)
# obj.get("foo", 4)
# obj.get("foo", 5)
