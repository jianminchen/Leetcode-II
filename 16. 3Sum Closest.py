import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        res=sys.maxint
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                temp=nums[i]+nums[left]+nums[right]
                if temp==target:
                    return temp
                elif temp>target:
                    right-=1
                else:
                    left+=1
                res=temp if abs(temp-target)<abs(res-target) else res 
        return res
