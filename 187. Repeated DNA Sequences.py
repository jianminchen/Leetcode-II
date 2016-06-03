class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic={}
        s=list(s)
        res=[]
        for i in xrange(len(s)-9):
            substring="".join(s[i:i+10])
            if substring not in dic:
                dic[substring]=1
            elif dic[substring]==1:
                res+=[substring]
                dic[substring]+=1
        return res
