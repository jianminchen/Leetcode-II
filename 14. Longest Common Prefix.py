class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        res=""
        ind=0
        while True:
            temp=""
            for str in strs:
                if ind<len(str):
                    if temp=="":
                        temp=str[ind]
                    else:
                        if temp!=str[ind]:
                            return res
                else:
                    return res
            res+=temp
            ind+=1
