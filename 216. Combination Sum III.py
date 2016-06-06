class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates=[i for i in xrange(1,10)]
        self.res=[]
        self.k=k
        self.candidates=candidates
        self.cs([], 0, n)
        return self.res
        
    def cs(self, path, start, target):
        if target==0 and len(path)==self.k:
            self.res+=[path[:]]
            return
        for i in xrange(start,len(self.candidates)):
            if self.candidates[i]<=target:
                path+=[self.candidates[i]]
                self.cs(path, i+1, target-self.candidates[i])
                path.pop()
