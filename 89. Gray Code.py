class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        initial=[0]
        for i in xrange(n):
            length=len(initial)
            for j in xrange(length-1,-1,-1):
                initial+=[initial[j]+(1<<i)]
        return initial
