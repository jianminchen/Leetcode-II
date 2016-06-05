class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        for i in xrange(n):
            length=len(res)
            for j in xrange(length-1,-1,-1):
                res+=[res[j]+(1<<i)]
        return res
