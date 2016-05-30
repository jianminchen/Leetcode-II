class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        index=1
        pre=nums[0]
        i=1
        while i<len(nums):
            if nums[i]>pre:
                nums[index]=nums[i]
                pre=nums[i]
                index+=1
                i+=1
            else:
                nums.pop(i)
        return len(nums)
