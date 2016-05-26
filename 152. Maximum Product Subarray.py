class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
            
        T=[0 for i in xrange(n+1)]
        T[1]=(nums[0],nums[0]) #(min,max)
        res=nums[0]
        
        for i in xrange(2,n+1):
            if nums[i-1]>0:
                maxx=max(T[i-1][1]*nums[i-1],nums[i-1])
                minn=min(T[i-1][0]*nums[i-1],nums[i-1])
            else:
                maxx=max(T[i-1][0]*nums[i-1],nums[i-1])
                minn=min(T[i-1][1]*nums[i-1],nums[i-1])
            T[i]=(minn,maxx)
            res=max(res,maxx)
        return res
