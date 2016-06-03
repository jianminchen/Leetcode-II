#timeout

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        number=1
        index2=1
        index3=1
        index5=1
        while number<num:
            number=min(2*index2,3*index3,5*index5)
            if number==2*index2:
                index2+=1
            elif number==3*index3:
                index3+=1
            elif number==5*index5:
                index5+=1
        if number==num:
            return True
        return False
