class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        self.res=[]
        self.n=len(nums)
        self.nums=nums
        self.k=0
        self.pre={}
        while self.k<=self.n:
            self.combination([], 0)
            self.k+=1
        return self.res
        
    def combination(self, path, start):
        if self.k==len(path):
            if tuple(path) not in self.pre:
                self.res+=[path[:]]
                self.pre[tuple(path)]=1
            return
        for i in xrange(start, self.n):
            path+=[self.nums[i]]
            self.combination(path, i+1)
            path.pop()
