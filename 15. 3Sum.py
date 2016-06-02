#timeout

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        twosum={}
        res=[]
        nums=sorted(nums)
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[i]+nums[j] not in twosum:
                    twosum[nums[i]+nums[j]]=[]
                twosum[nums[i]+nums[j]]+=[[i,j]]
        for k in xrange(len(nums)):
            if -nums[k] in twosum:
                for pair in twosum[-nums[k]]:
                    if k>pair[0] and k>pair[1]:
                        temp=sorted([nums[pair[0]], nums[pair[1]], nums[k]])
                        if (temp[0],temp[1],temp[2]) not in res:
                            res.append((temp[0],temp[1],temp[2]))
        res=sorted(res)
        return res
