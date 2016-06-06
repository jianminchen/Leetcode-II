class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num)==0:
            return []
        if len(num)==1:
            return [num]
        num.sort()
        res=[]
        pre=None
        for i in range(len(num)):
            if num[i]!=pre:
                pre=num[i]
                for j in self.permuteUnique(num[:i]+num[i+1:]):
                    res.append([num[i]]+j)
        return res
