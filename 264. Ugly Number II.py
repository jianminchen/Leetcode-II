class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        T=[0 for i in xrange(n)]
        T[0]=1
        
        index2=0
        index3=0
        index5=0
        for i in xrange(1,n):
            T[i]=min(2*T[index2],3*T[index3],5*T[index5])
            if T[i]==2*T[index2]:
                index2+=1
            if T[i]==3*T[index3]:
                index3+=1
            if T[i]==5*T[index5]:
                index5+=1
        return T[n-1]
