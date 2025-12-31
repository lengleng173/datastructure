# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
from collections import deque
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k=k
        self.items=[0]*self.k
        
        self.top=0
        self.tail=0
        self.flag=False

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.flag=True
        self.items[self.tail]=value
        self.tail=(self.tail+1)%self.k
        
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.flag=False
        self.top=(self.top+1)%self.k
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.top]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[(self.tail-1+self.k)%self.k]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.top==self.tail and self.flag==False

    def isFull(self):
        """
        :rtype: bool
        """
        return self.top==self.tail and self.flag==True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()