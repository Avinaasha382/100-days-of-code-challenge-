class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, val):
        self.top += 1
        self.stack.append(val)

    def pop(self):
        self.top -= 1

    def peek(self):
        return self.stack[self.top]
