class Solution:
    closure = {
        "{": "}",
        "[": "]",
        "(": ")",
    }

    def isValid(self, s: str) -> bool:
        stack = []
        while s:
            if s[0] in "({[":
                stack.append(s[0])
            elif s[0] in ")}]":
                try:
                    bracket = stack.pop()
                    if self.closure[bracket] != s[0]:
                        return False
                except IndexError:
                    return False

            s = s[1:]

        if stack:
            return False

        return True


print(Solution().isValid("))"))
