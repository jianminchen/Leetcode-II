class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums={}
        nums['I']=1
        nums['V']=5
        nums['X']=10
        nums['L']=50
        nums['C']=100
        nums['D']=500
        nums['M']=1000
        res=0
        for i in xrange(len(s)):
            if i>0 and nums[s[i]]>nums[s[i-1]]:
                res+=nums[s[i]]-2*nums[s[i-1]]
            else:
                res+=nums[s[i]]
        return res
