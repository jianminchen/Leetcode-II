class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern=list(pattern)
        str=str.split(" ")
        if len(pattern)!=len(str):
            return False
        dic={}
        for i in xrange(len(pattern)):
            if pattern[i] not in dic:
                if str[i] not in dic.values():
                    dic[pattern[i]]=str[i]
                else:
                    return False
            else:
                if dic[pattern[i]]!=str[i]:
                    return False
        return True
