class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x/10==0:
            return True
        if x%10==0:
            return False
        sum=0
        while x>0:
            sum=sum*10+x%10
            if sum==x or sum==x/10:
                return True
            x/=10
        return False
