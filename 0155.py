class MinStack:
    def __init__(self):
        self.s: list[tuple] = []

    def push(self, val: int) -> None:
        if self.s:
            new_min = min(val, self.s[-1][1])
        else:
            new_min = val
        self.s.append((val, new_min))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
