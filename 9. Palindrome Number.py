class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x/10==0:
            return True
        if x%10==0: #ex: 10, 100
            return False
        sum=0
        while x>0:
            sum=sum*10+x%10
            if sum==x or sum==x/10: #depends on length of x is odd or even
                return True
            x/=10
        return False
