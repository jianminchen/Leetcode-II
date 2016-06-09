class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=""
        while n>0:
            res=chr(ord('A')+(n-1)%26)+res
            n=(n-1)/26
        return res
