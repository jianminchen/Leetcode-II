class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        con_s={}
        con_t={}
        for i,j in zip(s,t):
            if i not in con_s:
                con_s[i]=j
            if j not in con_t:
                con_t[j]=i
            if con_s[i]!=j or con_t[j]!=i:
                return False
        return True
