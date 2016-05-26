class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        T=[[0 for j in xrange(i)] for i in xrange(n+1)] #calculate the minimum path for each element in the triangle
        T[1][0]=triangle[0][0]
        
        for i in xrange(2,n+1):
            for j in xrange(i):
                if j==0:
                    T[i][j]=T[i-1][j]+triangle[i-1][j]
                elif j==i-1:
                    T[i][j]=T[i-1][j-1]+triangle[i-1][j]
                else:
                    T[i][j]=min(T[i-1][j]+triangle[i-1][j],T[i-1][j-1]+triangle[i-1][j])
        return min(T[n])
