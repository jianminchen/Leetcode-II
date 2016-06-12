class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dic={}
        res=[]
        exists={}
        nums=sorted(nums)
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[i]+nums[j] not in dic:
                    dic[nums[i]+nums[j]]=[]
                dic[nums[i]+nums[j]]+=[(i,j)]
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                temp=target-(nums[i]+nums[j])
                if temp in dic:
                    for k in dic[temp]:
                        if k[0]>i and k[0]>j and k[1]>i and k[1]>j:
                            if (nums[i], nums[j], nums[k[0]], nums[k[1]]) not in exists:
                                res+=[[nums[i], nums[j], nums[k[0]], nums[k[1]]]]
                                exists[(nums[i], nums[j], nums[k[0]], nums[k[1]])]=1
        return res
