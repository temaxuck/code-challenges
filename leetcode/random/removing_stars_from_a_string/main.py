class Solution:
    def removeStars(self, s: str) -> str:
        r = []

        for c in s:
            if c == "*":
                r.pop()
            else:
                r.append(c)

        return "".join(r)


if __name__ == "__main__":
    print(Solution().removeStars("leet**cod*e"))
