class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res=0
        self.nqueens([], n)
        return self.res
    
    def isvalid(self, path, current):
        for i in xrange(len(path)):
            if path[i]==current or abs(path[i]-current)==len(path)-i:
                return False
        return True
    
    def nqueens(self, path, n):
        if len(path)==n:
            self.res+=1
        for i in xrange(n):
            if i not in path and self.isvalid(path, i):
                path+=[i]
                self.nqueens(path, n)
                path.pop()
