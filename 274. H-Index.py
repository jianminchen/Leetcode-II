class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)==0:
            return 0
        citations=sorted(citations, reverse=True)
        for i in xrange(1,len(citations)):
            if citations[i-1]>=i and citations[i]<=i:
                return i
        return min(min(citations),len(citations))
