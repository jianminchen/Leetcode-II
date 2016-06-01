class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        T=[0 for i in xrange(len(nums))]
        for i in xrange(len(nums)):
            T[i]=max(T[i-1],i+nums[i])
            if i<len(nums)-1 and T[i]<i+1:
                return False
                break
        return True
