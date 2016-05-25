class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        T=[[0 for j in xrange(n+1)] for i in xrange(m+1)]
        if obstacleGrid[0][0]==0:
            T[1][1]=1
        for i in xrange(2,m+1):
            if obstacleGrid[i-1][1-1]==0 and T[i-1][1]==1:
                T[i][1]=1
        for j in xrange(2,n+1):
            if obstacleGrid[1-1][j-1]==0 and T[1][j-1]==1:
                T[1][j]=1
        for i in xrange(2,m+1):
            for j in xrange(2,n+1):
                if obstacleGrid[i-1][j-1]==0:
                    T[i][j]+=T[i][j-1]
                    T[i][j]+=T[i-1][j]
        return T[m][n]
