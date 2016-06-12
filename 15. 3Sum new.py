class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        exists={}
        res=[]
        nums=sorted(nums)
        for i in xrange(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=i
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                temp=-(nums[i]+nums[j])
                if temp in dic:
                    if i>dic[temp] and j>dic[temp]:
                        if (nums[dic[temp]], nums[i], nums[j]) not in exists:
                            res+=[[nums[dic[temp]], nums[i], nums[j]]]
                            exists[(nums[dic[temp]], nums[i], nums[j])]=1
        return sorted(res)
