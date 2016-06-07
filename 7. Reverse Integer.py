class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint=2147483647
        if x>=0:
            temp=int(str(x)[::-1])
            if temp>=maxint:
                return 0
            return temp
        else:
            temp=-int(str(-x)[::-1])
            if temp<=-maxint:
                return 0
            return temp
