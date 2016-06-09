class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        b=1
        for i in s[::-1]:
            res+=(ord(i)-ord('A')+1)*b
            b*=26
        return res
