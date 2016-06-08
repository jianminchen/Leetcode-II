class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [str(nums[0])]
        begin=nums[0]
        end=nums[0]
        res=[]
        for i in xrange(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                end=nums[i]
            else:
                if begin==end:
                    res+=[str(begin)]
                else:
                    res+=[str(begin)+"->"+str(end)]
                begin=nums[i]
                end=nums[i]
        if begin==end:
            res+=[str(begin)]
        else:
            res+=[str(begin)+"->"+str(end)]
        return res
