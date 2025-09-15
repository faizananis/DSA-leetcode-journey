class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            minimum=min(val,self.stack[-1][-1])
            self.stack.append((val,minimum))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        t=self.stack[-1]
        return t[0]

    def getMin(self) -> int:
        t=self.stack[-1]
        return t[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()