class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n=len(s)
        T=[False for i in xrange(n+1)]
        T[0]=True
        for i in xrange(1,n+1):
            for j in xrange(1,i+1):
                if T[j-1] and s[j-1:i] in wordDict:
                    T[i]=True
        return T[n]
