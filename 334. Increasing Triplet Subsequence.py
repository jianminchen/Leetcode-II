# timeout

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        T=[1 for i in xrange(len(nums))]
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i]>nums[j]:
                    T[i]=max(T[i],T[j]+1)
                if T[i]>=3:
                    return True
        return False
