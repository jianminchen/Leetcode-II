class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        self.n=len(nums)
        self.nums=nums
        self.k=0
        while self.k<=self.n:
            self.combination([], 0)
            self.k+=1
        return self.res
        
    def combination(self, path, start):
        if self.k==len(path):
            self.res+=[path[:]]
            return
        for i in xrange(start, self.n):
            path+=[self.nums[i]]
            self.combination(path, i+1)
            path.pop()
