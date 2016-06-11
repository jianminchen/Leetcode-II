class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def compare(x, y):
            if x+y>y+x:
                return 1
            elif x+y<y+x:
                return -1
            else:
                return 0
        res=""
        for n in reversed(sorted(map(str,num),cmp=compare)):
            res+=n
        if res[0]=='0':
            return '0'
        return res
