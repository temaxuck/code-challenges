class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("Stack is empty")

        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("Stack is empty")

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

    def __str__(self) -> str:
        return str(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj)
val = 1
obj.push(val)
print(obj)
obj.pop()
print(obj)
obj.push(1)
obj.push(2)
obj.push(3)
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
