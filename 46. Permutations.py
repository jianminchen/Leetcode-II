class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[[nums[0]]]
        for i in xrange(1,n):
            cur_res=[]
            for j in res:
                temp=[]
                temp[:]=j[:]
                temp.insert(len(j),nums[i])
                cur_res+=[temp]
                for l in xrange(1,len(j)):
                    temp=[]
                    temp[:]=j[:]
                    temp.insert(l,nums[i])
                    cur_res+=[temp]
                temp=[]
                temp[:]=j[:]
                temp.insert(0,nums[i])
                cur_res+=[temp]
            res=cur_res
        return res
