class MyStack(object):

    def __init__(self):
        self.stack = []
        self.head = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.head += 1

    def pop(self):
        """
        :rtype: int
        """
        r = self.stack.pop()
        self.head = -1
        return r

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.head]

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()