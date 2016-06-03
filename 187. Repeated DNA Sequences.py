class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic={}
        res=[]
        for i in xrange(len(s)-9):
            substring=s[i:i+10]
            if substring not in dic:
                dic[substring]=1
            elif dic[substring]==1:
                res+=[substring]
                dic[substring]+=1
        return res
