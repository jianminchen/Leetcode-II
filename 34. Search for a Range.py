class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin=0
        end=0
        for i in xrange(1,len(nums)):
            if nums[0]!=target and nums[i]==target and nums[i-1]!=target:
                begin=i
            if nums[i-1]==target:
                if nums[i]!=target:
                    end=i-1
                    break
        if nums[len(nums)-1]==target:
            end=len(nums)-1
        if begin==0 and end==0 and nums[0]!=target:
            return [-1,-1]
        return [begin,end]
