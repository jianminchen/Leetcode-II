class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        T=[0 for i in xrange(n+1)]
        T[1]=10
        for k in xrange(2,n+1):
            T[k]=9
            temp=9
            while temp>=9-k+2:
                T[k]*=temp
                temp-=1
        return sum(T)
