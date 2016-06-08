class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn=nums[0]
        for i in xrange(1,len(nums)):
            if nums[i]>nums[i-1]:
                continue
            else:
                minn=min(minn,nums[i])
        return minn
