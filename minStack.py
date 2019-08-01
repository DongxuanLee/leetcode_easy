class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.order_stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.order_stack or self.stack[self.order_stack[-1]]>x:
            self.order_stack.append(len(self.stack)-1)
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.stack) ==self.order_stack[-1]:
            self.order_stack.pop()
    def top(self):
        """
        :rtype: int
        """
        param_3 = self.stack[-1]
        return param_3
    def getMin(self):
        """
        :rtype: int
        """
        param_4 = self.stack[self.order_stack[-1]]
        return param_4



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()