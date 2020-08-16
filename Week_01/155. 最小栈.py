# https://leetcode-cn.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        self.min = float("inf")
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min:
            self.min = x
        self.minstack.append(self.min)

    def pop(self) -> None:
        self.stack.__delitem__(-1)
        self.minstack.__delitem__(-1)
        if self.minstack: self.min = self.minstack[-1]
        else: self.min = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()