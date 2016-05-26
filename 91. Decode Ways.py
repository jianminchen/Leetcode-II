class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        elif n==1 and int(s)>=1:
            return 1
        elif n==1 and int(s)==0:
            return 0
        elif n>1 and int(s[0])==0:
            return 0
            
        T=[0 for i in xrange(n+1)]
        T[1]=1
        if int(s[1])>=1:
            if int(s[0])>=1:
                if int(s[0:2])<=26: 
                    T[2]=2
                else:
                    T[2]=1
        elif int(s[0])>=1 and int(s[1])==0:
            if int(s[0:2])<=26:
                T[2]=1
        for i in xrange(3,n+1):
            if int(s[i-1])>=1:
                if int(s[i-2])>=1 and int(s[i-2:i])<=26:
                    T[i]=T[i-1]+T[i-2]
                else:
                    T[i]=T[i-1]
            else:
                if int(s[i-2])>=1 and int(s[i-2:i])<=26:
                    T[i]=T[i-2]
                else:
                    return 0
        print T
        return T[n]
