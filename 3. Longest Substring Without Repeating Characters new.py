import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        res=0
        dic={}
        for i in xrange(len(s)):
            dic[s[i]]=-1
        for i in xrange(len(s)):
            if dic[s[i]]!=-1:
                while start<=dic[s[i]]:
                    dic[s[start]]=-1
                    start+=1
            res=max(res, i-start+1)
            dic[s[i]]=i
        return res
