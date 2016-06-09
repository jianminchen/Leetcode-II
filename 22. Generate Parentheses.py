class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res=[]
        numl, numr=0, 0
        self.Parenthesis(numl, numr, "", n)
        return self.res
        
    def Parenthesis(self, numl, numr, path, n):
        if len(path)==2*n:
            self.res+=[path[:]]
        if numl<n:
            self.Parenthesis(numl+1, numr, path+'(', n)
        if numr<numl:
            self.Parenthesis(numl, numr+1, path+')', n)
