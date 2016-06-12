# timeout

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        res=0
        i=0
        while i<len(s):
            if s[i] not in dic:
                dic[s[i]]=i
            else:
                res=max(res, i-dic[s[i]])
                t=i
                i=dic[s[i]]
                dic[s[i]]=t
            i+=1
        return res
