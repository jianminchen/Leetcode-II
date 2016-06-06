class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res=[]
        self.n, self.k=n, k
        self.combination([], 1)
        return self.res
        
    def combination(self, path, start):
        if self.k==len(path):
            self.res+=[path[:]]
            return
        for i in xrange(start, self.n+1):
            path+=[i]
            self.combination(path, i+1)
            path.pop()
