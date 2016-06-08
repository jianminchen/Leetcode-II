class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        i=0
        while i<len(s):
            if s[i]=="":
                del s[i]
            else:
                i+=1
        if len(s)==0:
            return ""
        return ' '.join(s[::-1])
