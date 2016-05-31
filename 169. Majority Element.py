import operator

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        sorted_dic=sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        return sorted_dic[0][0]
