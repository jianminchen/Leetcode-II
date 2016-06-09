class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res=[]
        self.n=n
        self.Parenthesis(0, 0, "")
        return self.res
        
    def Parenthesis(self, numl, numr, path):
        if len(path)==2*self.n:
            self.res+=[path[:]]
        if numl<self.n:
            self.Parenthesis(numl+1, numr, path+'(')
        if numr<numl:
            self.Parenthesis(numl, numr+1, path+')')
