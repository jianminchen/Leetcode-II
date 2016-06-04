class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split(" ")
        for i in xrange(len(s)-1,-1,-1):
            if s[i]!=u'':
                return len(s[i])
        return 0
