class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in xrange(1,len(prices)):
            temp=prices[i]-prices[i-1]
            if temp>0:
                profit+=temp
        return profit
