class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=len(matrix)
        for i in xrange(m):
            matrix[i]=map(int,matrix[i])
        if m>0:
            n=len(matrix[0])
        if m==0:
            return 0
            
        T=[[0 for j in xrange(n)] for i in xrange(m)]
        maxx=0
        for i in xrange(m):
            T[i][0]=matrix[i][0]
            maxx=max(maxx,T[i][0])
        for j in xrange(n):
            T[0][j]=matrix[0][j]
            maxx=max(maxx,T[0][j])
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j]==1:
                    T[i][j]=min(T[i-1][j],T[i][j-1],T[i-1][j-1])+1
                    maxx=max(maxx,T[i][j])
        return maxx**2
