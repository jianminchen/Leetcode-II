class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or sum(nums)<s:
            return 0
        minn=len(nums)+1
        start=0
        for i in xrange(1,len(nums)+1):
            while sum(nums[start:i])>=s:
                minn=min(minn,i-start)
                start+=1
        return minn
