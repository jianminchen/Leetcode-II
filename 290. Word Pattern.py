class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str=str.split(" ")
        if len(pattern)!=len(str):
            return False
        dic={}
        strlist={}
        for i in xrange(len(pattern)):
            if pattern[i] not in dic:
                if str[i] not in strlist:
                    dic[pattern[i]]=str[i]
                    strlist[str[i]]=1
                else:
                    return False
            else:
                if dic[pattern[i]]!=str[i]:
                    return False
        return True
