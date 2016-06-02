class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s=sorted(list(s))
        sorted_t=sorted(list(t))
        if sorted_s==sorted_t:
            return True
        return False
