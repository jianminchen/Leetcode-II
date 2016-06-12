class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res=0
        self.nqueens([], n)
        return self.res
    
    def isvalid(self, path):
        for i in xrange(1,len(path)):
            for j in xrange(i):
                if path[i]==path[j] or abs(path[i]-path[j])==i-j:
                    return False
        return True
    
    def nqueens(self, path, n):
        if len(path)==n:
            self.res+=1
        for i in xrange(n):
            if i not in path:
                path+=[i]
                if self.isvalid(path):
                    self.nqueens(path, n)
                path.pop()
