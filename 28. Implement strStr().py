class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            temp=haystack.index(needle)
            return temp
        except:
            return -1
