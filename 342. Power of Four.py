class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n<=0:
            return False
        log=float(math.log10(n)/math.log10(4))
        if log-int(log)==0:
            return True
        return False
