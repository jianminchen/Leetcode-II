class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        T=[0 for i in xrange(len(nums)+1)] #T[i]=the max sum of subarray which ends at i
        T[1]=nums[0]
        maxx=nums[0]
        for i in xrange(2,len(nums)+1):
            T[i]=max(T[i-1]+nums[i-1],nums[i-1])
            maxx=max(maxx,T[i])
        return maxx
