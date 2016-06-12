class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        if len(nums)==0:
            return []
        nums=sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                temp=nums[i]+nums[left]+nums[right]
                if temp==0:
                    res+=[[nums[i], nums[left], nums[right]]]
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif temp>0:
                    right-=1
                else:
                    left+=1
        return res
