class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        div=n/3
        if div<=1:
            return (n / 2) * (n / 2 + n % 2)
        mod=n%3
        if mod==0:
            return 3 ** div
        elif mod==1:
            return 3 ** (div - 1) * 4
        elif mod==2:
            return 3 ** div * 2
