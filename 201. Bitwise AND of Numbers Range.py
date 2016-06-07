class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        bin_m=bin(m)[2:]
        bin_n=bin(n)[2:]
        while len(bin_m)<len(bin_n):
            bin_m="0"+bin_m
        res=""
        for i in xrange(len(bin_n),0,-1):
            if bin_m[:i]!=bin_n[:i]:
                res="0"+res
            else:
                res=str(int(bin_m[i-1]) & int(bin_n[i-1]))+res
        return int(res,2)
