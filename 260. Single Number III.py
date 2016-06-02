class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        res=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            elif dic[i]==2:
                del dic[i]
            else:
                dic[i]+=1
        
        for i in dic:
            if dic[i]==1:
                res+=[i]
        return res
