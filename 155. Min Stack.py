import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minn=sys.maxint

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minn=min(self.minn,x)
        self.stack+=[x]
        

    def pop(self):
        """
        :rtype: void
        """
        temp=self.stack.pop()
        if temp==self.minn:
            if len(self.stack)>0:
                self.minn=min(self.stack)
            else:
                self.minn=sys.maxint
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minn
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
