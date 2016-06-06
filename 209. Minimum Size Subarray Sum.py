# timeout

import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minn=sys.maxint
        if len(nums)==0:
            return 0
        for i in xrange(1,len(nums)+1):
            if nums[i]>=s:
                return 1
            for j in xrange(i+1):
                if sum(nums[j:i+1])>=s:
                    minn=min(minn,i+1-j)
        if minn==sys.maxint:
            return 0
        return minn
