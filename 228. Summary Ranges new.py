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
        begin=end=0
        res=[]
        while end<len(nums):
            if end+1<len(nums) and nums[end+1]==nums[end]+1:
                end+=1
            else:
                if begin==end:
                    res+=[str(nums[begin])]
                else:
                    res+=[str(nums[begin])+"->"+str(nums[end])]
                end+=1
                begin=end
        return res
