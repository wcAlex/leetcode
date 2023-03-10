class MyQueue:

    def __init__(self):
        self.stack_in= []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if len(self.stack_out) == 0:
            while len(self.stack_in):
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out.pop()

    def peek(self) -> int:
        if len(self.stack_out) == 0:
            while len(self.stack_in):
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out[-1]

    def empty(self) -> bool:
        return len(self.stack_in) + len(self.stack_out) == 0 