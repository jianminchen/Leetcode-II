class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        en=1
        for i in xrange(len(digits)-1,-1,-1):
            if digits[i]+en<=9:
                digits[i]+=en
                en=0
            else:
                digits[i]=0
                en=1
        if en==1:
            digits.insert(0,1)
        return digits
