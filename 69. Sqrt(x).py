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
            temp=mid**2
            if temp<x:
                i=mid+1
            elif temp>x:
                j=mid-1
            else:
                return mid
        return j
