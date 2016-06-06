class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        self.res=[]
        self.nums=nums
        self.k=0
        self.pre={}
        while self.k<=len(self.nums):
            self.combination([], 0)
            self.k+=1
        return self.res
        
    def combination(self, path, start):
        if self.k==len(path):
            self.res+=[path[:]]
            return
        for i in xrange(start, len(self.nums)):
            if i!=start and self.nums[i]==self.nums[i-1]:
                continue
            path+=[self.nums[i]]
            self.combination(path, i+1)
            path.pop()
