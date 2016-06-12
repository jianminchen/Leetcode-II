class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        l=len(s)
        if l<=2:
            if s[0]!=s[l-1]:
                return ''
            else:
                return s
        for i in xrange(l):
            p=self.palin(s, i, i)
            if len(p)>len(res):
                res=p
            p=self.palin(s, i, i+1)
            if len(p)>len(res):
                res=p
        return res
                    
    def palin(self, s, begin, end):
        while begin>=0 and end<len(s) and s[begin]==s[end]:
            begin-=1
            end+=1
        return s[begin+1:end]
