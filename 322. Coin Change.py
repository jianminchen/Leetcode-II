class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        if n==1 and amount!=0:
            if amount%coins[0]==0 and amount/coins[0]>0:
                return amount/coins[0]
            else:
                return -1
        T=[-1 for i in xrange(amount+1)]
        T[0]=0
        for j in coins:
            if j<=amount:
                T[j]=1
        for i in xrange(1,amount+1):
            temp=amount+1
            for j in coins:
                if i>=j and T[i-j]!=-1:
                    temp=min(temp,T[i-j]+1)
            if temp<amount+1:
                T[i]=temp
        return T[amount]
