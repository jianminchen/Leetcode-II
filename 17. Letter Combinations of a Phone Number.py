class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.buttons=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        if len(digits)==0:
            return []
        elif len(digits)==1:
            return self.buttons[int(digits)]
        self.digits=digits
        self.res=[]
        self.combination([])
        return self.res
        
    def combination(self, path):
        if len(path)==len(self.digits):
            self.res+=["".join(path)]
            return
        for i in xrange(len(self.digits)):
            for j in self.buttons[int(self.digits[i])]:
                if len(path)==i:
                    path+=[j]
                    self.combination(path)
                    path.pop()
