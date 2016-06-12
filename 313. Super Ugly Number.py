# timeout

import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index=[0 for i in xrange(len(primes))]
        super_ugly=[1]
        
        while len(super_ugly)<n:
            minn=sys.maxint
            min_ind=0
            for i in xrange(len(primes)):
                if primes[i]*super_ugly[index[i]]<minn:
                    minn=primes[i]*super_ugly[index[i]]
                    min_ind=i
            if minn!=super_ugly[len(super_ugly)-1]:
                super_ugly+=[minn]
            index[min_ind]+=1
        return super_ugly[n-1]
