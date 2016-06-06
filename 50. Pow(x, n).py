class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>=0:
            try:
                return self.power(x, n)
            except OverflowError:
                return float(0)
        else:
            n=-n
            try:
                return float(1/self.power(x, n))
            except OverflowError:
                return float(0)
        
    def power(self, x, n):
        if n==0:
            return float(1)
        if n%2==0:
            return float(self.power(x, n/2)**2)
        else:
            return float(self.power(x, n/2)**2*x)
