class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=bin(n)[2:][::-1]
        while len(s)<32:
            s+="0"
        return int(s,2)
