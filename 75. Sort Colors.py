class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i=0
        num_of_2=0
        while i<len(nums):
            if nums[i]==0:
                nums.insert(0,nums.pop(i))
                i+=1
            elif nums[i]==2:
                num_of_2+=1
                nums.pop(i)
            else:
                i+=1
        for i in xrange(num_of_2):
            nums+=[2]
