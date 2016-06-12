# https://leetcode.com/discuss/72763/python-generators-on-a-heap

import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        super_ugly=[1]
        merged=heapq.merge(*map(lambda p: (u*p for u in super_ugly), primes))
        uniqed=(u for u, _ in itertools.groupby(merged))
        map(super_ugly.append, itertools.islice(uniqed, n-1))
        return super_ugly[n-1]
