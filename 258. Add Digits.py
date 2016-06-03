class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=map(int,list(str(num)))
        if len(n)==1:
            return num
        totalsum=0
        
        while len(n)>1:
            totalsum=sum(n)
            n=map(int,list(str(totalsum)))
        
        return totalsum
