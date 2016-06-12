class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.current_n=1
        self.matrix=[[n**2 for j in xrange(n)] for i in xrange(n)]
        self.DFS(n, 0, 0, 0, n-1, 1, n-1, "R")
        return self.matrix
        
    def DFS(self, n, i, j, xmin, xmax, ymin, ymax, direction):
        if self.current_n>=n**2:
            return
        if direction=="R":
            while j<xmax:
                self.matrix[i][j]=self.current_n
                j+=1
                self.current_n+=1
            if j==xmax:
                self.DFS(n, i, j, xmin, xmax-1, ymin, ymax, "D")
        elif direction=="D":
            while i<ymax:
                self.matrix[i][j]=self.current_n
                i+=1
                self.current_n+=1
            if i==ymax:
                self.DFS(n, i, j, xmin, xmax, ymin, ymax-1, "L")
        elif direction=="L":
            while j>xmin:
                self.matrix[i][j]=self.current_n
                j-=1
                self.current_n+=1
            if j==xmin:
                self.DFS(n, i, j, xmin+1, xmax, ymin, ymax, "U")
        elif direction=="U":
            while i>ymin:
                self.matrix[i][j]=self.current_n
                i-=1
                self.current_n+=1
            if i==ymin:
                self.DFS(n, i, j, xmin, xmax, ymin+1, ymax, "R")
