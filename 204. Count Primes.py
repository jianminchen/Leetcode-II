class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 0
        isprime=[True for i in xrange(n)]
        isprime[0], isprime[1]=False, False
        x=2
        while x*x<n:
            if isprime[x]:
                p=x*x
                while p<n:
                    isprime[p]=False
                    p+=x
            x+=1
        return sum(isprime)
