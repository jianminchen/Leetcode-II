class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=map(int,list(str(n)))
        dic={}
        
        while True:
            if tuple(n) not in dic:
                dic[tuple(n)]=1
                squaresum=sum([i**2 for i in n])
                if squaresum==1:
                    return True
                n=map(int,list(str(squaresum)))
            else:
                break
        return False
