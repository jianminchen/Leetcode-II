class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ind1=-1
        ind2=-1
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind1=i
                break
        if ind1<0:
            nums[:]=nums[::-1]
        else:
            for i in xrange(ind1+1,len(nums)):
                if nums[i]>nums[ind1]:
                    ind2=i
            temp=nums[ind1]
            nums[ind1]=nums[ind2]
            nums[ind2]=temp
            nums[:]=nums[:ind1+1]+nums[ind1+1:][::-1]
