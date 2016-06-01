class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        self.pascal=[]
        self.recursion([1], rowIndex)
        return self.pascal
        
    def recursion(self, prerow, nrows):
        if nrows==0:
            self.pascal=prerow
            return
        currentrow=[1]
        for i in xrange(1,len(prerow)):
            if i==1:
                currentrow+=[currentrow[len(currentrow)-1]+prerow[i]]
            else:
                currentrow+=[prerow[i]+prerow[i-1]]
        currentrow+=[1]
        self.recursion(currentrow, nrows-1)
