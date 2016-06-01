class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        self.pascal=[[1]]
        self.recursion([1], numRows-1)
        return self.pascal
        
    def recursion(self, prerow, nrows):
        if nrows==0:
            return
        currentrow=[1]
        for i in xrange(1,len(prerow)):
            if i==1:
                currentrow+=[currentrow[len(currentrow)-1]+prerow[i]]
            else:
                currentrow+=[prerow[i]+prerow[i-1]]
        currentrow+=[1]
        self.pascal.append(currentrow)
        self.recursion(currentrow, nrows-1)
