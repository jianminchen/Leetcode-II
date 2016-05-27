class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        T=[0 for i in xrange(n+1)]
        T[1]=nums[0]
        
        for i in xrange(2,n+1):
            T[i]=max(T[i-2]+nums[i-1],T[i-1])
        return T[n]
