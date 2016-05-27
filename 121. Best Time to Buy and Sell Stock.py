class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n==0 or n==1:
            return 0
        T=[0 for i in xrange(n+1)]
        
        minn=prices[0]
        for i in xrange(2,n+1):
            T[i]=prices[i-1]-minn
            minn=min(prices[i-1],minn)
        return max(T)
