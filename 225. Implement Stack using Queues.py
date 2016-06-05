class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1=[]
        self.queue2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1+=[x]

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.queue1)>1:
            self.queue2+=[self.queue1.pop(0)]
        temp=self.queue1.pop(0)
        while len(self.queue2)>0:
            self.queue1+=[self.queue2.pop(0)]
        return temp

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue1)>1:
            self.queue2+=[self.queue1.pop(0)]
        temp=self.queue1[0]
        self.queue2+=[self.queue1.pop(0)]
        while len(self.queue2)>0:
            self.queue1+=[self.queue2.pop(0)]
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1)==0
