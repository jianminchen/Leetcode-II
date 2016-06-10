class Solution:
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s): 
            return s
        res=[[] for row in xrange(numRows)]
        for i in range(len(s)): 
            res[numRows-1-abs(numRows-1-i % (2*numRows-2))].append(s[i])
        return "".join(["".join(res[i]) for i in xrange(numRows)])
