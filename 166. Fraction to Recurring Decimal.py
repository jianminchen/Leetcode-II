class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag=1
        if n<0 and d>0:
            n=-n
            flag=-1
        elif d<0 and n>0:
            d=-d
            flag=-1
        elif d<0 and n<0:
            n=-n
            d=-d
        if n%d==0:
            return str(flag*n/d)
        else:
            res="."
            m=n%d
            dic={}
            ind=1
            dic[m]=ind
            while m>0:
                temp1=(10*m)%d
                temp2=(10*m)/d
                res+=str(temp2)
                if temp1 in dic:
                    res=res[:dic[temp1]]+'('+res[dic[temp1]:]+')'
                    break
                ind+=1
                dic[temp1]=ind
                m=temp1
            if flag==-1:
                return '-'+str(n/d)+res
            return str(n/d)+res
