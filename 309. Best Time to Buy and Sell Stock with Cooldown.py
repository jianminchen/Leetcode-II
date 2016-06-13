class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n==0:
            return 0
        T=[[0 for j in xrange(2)] for i in xrange(n)]
        for i in xrange(1,n):
            T[i][0]=max(T[i-1][0], T[i-1][1]);
            T[i][1]=max(T[i-1][0], T[i-1][1]+prices[i]-prices[i-1])
        return max(T[n-1][0], T[n-1][1])
