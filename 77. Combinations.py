class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums=[i for i in xrange(1,n+1)]
        self.buttons=[nums]*k
        self.res=[]
        self.combination([], k)
        return self.res
        
    def combination(self, path, k):
        if len(path)==k:
            self.res+=[path[:]]
            return
        for i in xrange(k):
            for j in self.buttons[i]:
                if len(path)==i and (len(path)==0 or j>path[len(path)-1]):
                    path+=[j]
                    self.combination(path, k)
                    path.pop()
