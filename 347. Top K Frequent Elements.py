class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqlist={}
        for i in nums:
            if i not in freqlist:
                freqlist[i]=1
            else:
                freqlist[i]+=1
        freqlist=sorted(freqlist.items(), key=lambda x: x[1],reverse=True)
        res=[]
        for i in xrange(k):
            res+=[freqlist[i][0]]
        return res
