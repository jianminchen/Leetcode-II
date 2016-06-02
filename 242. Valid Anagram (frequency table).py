class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        s_letters=[0 for i in xrange(26)]
        t_letters=[0 for i in xrange(26)]
        
        for i in xrange(len(s)):
            s_letters[ord(s[i])-ord('a')]+=1
            t_letters[ord(t[i])-ord('a')]+=1
        
        if s_letters==t_letters:
            return True
        return False
