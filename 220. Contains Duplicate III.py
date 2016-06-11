# timeout

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if j-i<=k and abs(nums[j]-nums[i])<=t:
                    return True
        return False
