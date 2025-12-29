from collections import deque
class MyStack(object):
    
    def __init__(self):
        self.items=deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop()

    def top(self):
        """
        :rtype: int
        """ 
        x=self.items.pop()
        self.items.append(x)
        return x

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.items)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()