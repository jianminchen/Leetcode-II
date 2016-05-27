class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        T1=[0 for i in xrange(n)]
        T2=[0 for i in xrange(n)]
        for i in xrange(1,n):
            T1[i]=max(T1[i-2]+nums[i],T1[i-1])
        for i in xrange(n-1):
            T2[i]=max(T2[i-2]+nums[i],T2[i-1])
        return max(T1[n-1],T2[n-2])
