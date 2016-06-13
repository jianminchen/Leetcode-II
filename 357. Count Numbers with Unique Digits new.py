class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        res=0
        res+=10
        for k in xrange(2,n+1):
            uniqles_with_len_k=9
            temp=9
            while temp>=9-k+2:
                uniqles_with_len_k*=temp
                temp-=1
            res+=uniqles_with_len_k
        return res
