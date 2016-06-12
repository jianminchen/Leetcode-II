class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        for i in xrange(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
