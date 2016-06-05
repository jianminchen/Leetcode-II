class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k-=1 # to 0-based
        nums=[i for i in xrange(1,n+1)]
        fractorial=1
        for i in xrange(2,n):
            fractorial*=i
        res=""
        while len(nums)>0:
            res+=str(nums.pop(k/fractorial))
            k%=fractorial
            if len(nums)>0:
                fractorial/=len(nums)
        return res
