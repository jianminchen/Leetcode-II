class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        i=0
        j=len(s)-1
        while i<j:
            while i<=len(s)-1 and not ((ord(s[i])>=ord('0') and ord(s[i])<=ord('9')) or (ord(s[i])>=ord('a') and ord(s[i])<=ord('z'))):
                i+=1
            while j>=0 and not ((ord(s[j])>=ord('0') and ord(s[j])<=ord('9')) or (ord(s[j])>=ord('a') and ord(s[j])<=ord('z'))):
                j-=1
            if i<j and s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
