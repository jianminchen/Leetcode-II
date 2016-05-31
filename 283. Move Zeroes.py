class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        znum=0
        while i<len(nums):
            if nums[i]==0:
                znum+=1
                del nums[i]
            else:
                i+=1
        for i in xrange(znum):
            nums.append(0)
