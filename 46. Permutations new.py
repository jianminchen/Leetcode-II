class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        self.nums=nums
        self.res=[]
        self.permutation([])
        return self.res
        
    def permutation(self, path):
        if len(path)==len(self.nums):
            self.res+=[path[:]]
            return
        for i in self.nums:
            if i not in path:
                path+=[i]
                self.permutation(path)
                path.pop()
