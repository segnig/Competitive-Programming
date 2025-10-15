# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.store = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack and self.min_stack[-1] >= val:
            self.min_stack.append(val)

        elif not self.min_stack:
            self.min_stack.append(val)
        
        self.store.append(val)


    def pop(self) -> None:
        val = self.store.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()