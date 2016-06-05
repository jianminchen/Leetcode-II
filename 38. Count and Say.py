class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq="1"
        if n==1:
            return '1'
        count=0
        for i in xrange(1,n):
            say=""
            for i in xrange(len(seq)):
                if i>=1:
                    if seq[i]!=seq[i-1]:
                        say+=str(count)+seq[i-1]
                        count=1
                    else:
                        count+=1
                else:
                    count=1
            say+=str(count)+seq[len(seq)-1]
            seq=say
        return say
