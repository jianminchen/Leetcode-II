class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos=0
        if target<=nums[0]:
            return pos
        for i in xrange(len(nums)):
            if nums[i]==target:
                pos=i
            elif i>0 and nums[i-1]<target and nums[i]>target:
                pos=i
        if i==len(nums)-1 and target>nums[i]:
                pos=i+1
        return pos
