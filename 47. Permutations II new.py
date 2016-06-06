class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        res=[]
        firstnums=[]
        firstnums[:]=nums[:]
        while True:
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

            if nums!=firstnums:
                res+=[nums[:]]
            else:
                res+=[nums[:]]
                break
        return res
