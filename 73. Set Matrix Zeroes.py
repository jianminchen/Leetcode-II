class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zerolist=[]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j]==0:
                   zerolist+=[(i,j)]
        print zerolist
        for z in zerolist:
            for j in xrange(len(matrix[0])):
                matrix[z[0]][j]=0
            for i in xrange(len(matrix)):
                matrix[i][z[1]]=0
