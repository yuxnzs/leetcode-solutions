class MinStack:

    def __init__(self):
        self.stack = []
        # 記錄每次 push 後，目前 stack 對應位置的最小值
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # 第一次 push 時，val 本身就是目前最小值
        if not self.minStack:
            value = val
        else:
            value = min(self.getMin(), val)

        self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
