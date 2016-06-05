# timeout

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res=["1"]
        for i in xrange(2,n+1):
            temp=[]
            for j in xrange(len(res)):
                temp+=[res[j][:]+str(i)]
                for l in xrange(1,len(res[0])):
                    temp+=[res[j][0:l]+str(i)+res[j][l:len(res)]]
                temp+=[str(i)+res[j][:]]
            res=temp
        res=sorted(res)
        return res[k-1]
