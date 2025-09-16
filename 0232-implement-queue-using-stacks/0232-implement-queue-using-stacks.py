class MyQueue:

    def __init__(self):
        self.main_stack = []   # for adding new elements
        self.temp_stack = []   # for removing/peeking elements

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        # if temp_stack is empty, move everything from main_stack
        if not self.temp_stack:
            while self.main_stack:
                self.temp_stack.append(self.main_stack.pop())
        return self.temp_stack.pop()

    def peek(self) -> int:
        # if temp_stack is empty, move everything from main_stack
        if not self.temp_stack:
            while self.main_stack:
                self.temp_stack.append(self.main_stack.pop())
        return self.temp_stack[-1]

    def empty(self) -> bool:
        return not self.main_stack and not self.temp_stack




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()