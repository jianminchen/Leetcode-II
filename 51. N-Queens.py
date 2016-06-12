class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res=[]
        self.nqueens([], n)
        return self.res
    
    def isvalid(self, path, current):
        for i in xrange(len(path)):
            if path[i]==current or abs(path[i]-current)==len(path)-i:
                return False
        return True
    
    def nqueens(self, path, n):
        if len(path)==n:
            temp=[]
            for i in xrange(len(path)):
                row=""
                for j in xrange(n):
                   if j!=path[i]:
                       row+="."
                   else:
                       row+="Q"
                temp+=[row]
            self.res+=[temp[:]]
        for i in xrange(n):
            if i not in path and self.isvalid(path, i):
                path+=[i]
                self.nqueens(path, n)
                path.pop()
