class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
            
        T=[0 for i in xrange(n+1)]
        T[0]=1
        T[1]=1

        for i in xrange(2,n+1):
            T[i]=sum([T[j]*T[i-1-j] for j in xrange(i)])
        return T[n]
