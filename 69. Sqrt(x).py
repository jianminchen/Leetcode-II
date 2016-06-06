class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return x
        i=0
        j=x/2+1
        while i<=j:
            mid=(i+j)/2
            if mid**2<x:
                i=mid+1
            elif mid**2>x:
                j=mid-1
            else:
                return mid
        return j
