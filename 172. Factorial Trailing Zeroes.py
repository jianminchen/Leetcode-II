class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        five=0
        while n>0:
            five+=n/5
            n/=5
        return five
