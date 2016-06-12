# timeout

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        n=len(s)
        L=[[0 for x in range(n)] for x in range(n)]
        for i in range(n):
            L[i][i]=1
            
        maxlength=0
        maxind=None
        for cl in range(2, n+1):
            for i in range(n-cl+1):
                j=i+cl-1
                if s[i]==s[j] and cl==2:
                    L[i][j]=2
                    if L[i][j]>maxlength:
                        maxlength=L[i][j]
                        maxind=(i,j)
                elif s[i]==s[j]:
                    if L[i+1][j-1]>0:
                        L[i][j]=L[i+1][j-1]+2
                    if L[i][j]>maxlength:
                        maxlength=L[i][j]
                        maxind=(i,j)
                else:
                    L[i][j]=0
        return s[maxind[0]:maxind[1]+1]
