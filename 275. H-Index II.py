class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l,r,n=0,len(citations),len(citations)
 
        while l<r:
            mid=(l + r)/2
            if n-mid<=citations[mid]:
                r=mid
            else:
                l=mid+1
 
        return n-l  
