import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        log=float(math.log10(n)/math.log10(3))
        if log-int(log)==0:
            return True
        return False
