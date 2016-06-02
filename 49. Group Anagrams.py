class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        res=[]
        group=0
        for i in strs:
            temp="".join(sorted(list(i)))
            if temp not in dic:
               dic[temp]=group
               group+=1
               res+=[[]]
            res[dic[temp]]+=[i]
        for i in xrange(len(res)):
            res[i]=sorted(res[i])
        return res
