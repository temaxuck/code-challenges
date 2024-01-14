from typing import List


class Solution:
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),
    }

    def to_number(self, s: str):
        try:
            return int(s)
        except ValueError:
            return None

    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        for token in tokens:
            if token in self.operations:
                r, l = values.pop(), values.pop()
                values.append(self.operations[token](l, r))
            else:
                values.append(int(token))

            print(values, token)

        if len(values) != 1:
            raise Exception(f"Invalid Reverse Polish Notation sequence: {tokens}")

        return values[0]


# print(Solution().evalRPN(["3", "11", "5", "+", "-"]))
print(Solution().evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))
print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
