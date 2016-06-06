class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []
        candidates=sorted(candidates)
        self.res=[]
        self.candidates=candidates
        self.cs([], 0, target)
        return self.res
        
    def cs(self, path, start, target):
        if target==0:
            self.res+=[path[:]]
            return
        for i in xrange(start,len(self.candidates)):
            if self.candidates[i]<=target:
                if i>start and self.candidates[i]==self.candidates[i - 1]:
                    continue
                path+=[self.candidates[i]]
                self.cs(path, i+1, target-self.candidates[i])
                path.pop()
