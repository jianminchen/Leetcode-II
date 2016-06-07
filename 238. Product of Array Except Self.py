class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1 for i in xrange(len(nums))]
        l=r=1
        for i in xrange(1,len(nums)):
            l*=nums[i-1]
            res[i]*=l
        for i in xrange(len(nums)-1,-1,-1):
            if i<len(nums)-1:
                r*=nums[i+1]
            res[i]*=r
        return res
