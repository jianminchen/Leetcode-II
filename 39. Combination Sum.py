class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []
        self.res=[]
        self.candidates=candidates
        self.cs([],0, target)
        return self.res
        
    def cs(self, path, start, target):
        if target==0:
            self.res+=[path[:]]
            return
        for i in xrange(start,len(self.candidates)):
            if self.candidates[i]<=target:
                path+=[self.candidates[i]]
                self.cs(path, i, target-self.candidates[i])
                path.pop()
