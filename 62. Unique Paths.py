class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        T=[[0 for j in xrange(n+1)] for i in xrange(m+1)]
        for i in xrange(1,m+1):
            T[i][1]=1
        for j in xrange(1,n+1):
            T[1][j]=1
        for i in xrange(2,m+1):
            for j in xrange(2,n+1):
                T[i][j]+=T[i-1][j]+T[i][j-1]
        return T[m][n]
