class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in xrange(1, len(num)):
            for j in xrange(i, len(num)):
                if self.isvalid(num, 0, i, j):
                    return True
        return False

    def isvalid(self, num, start, i, j):
        n1=num[start:i]
        n2=num[i:j]

        if start!=0 and j==len(num):
            return True
        if n1=="" or n2=="":
            return False
        if len(n1)>1 and n1[0]=='0' or len(n2)>1 and n2[0]=='0':
            return False

        n3=str(int(n1)+int(n2))
        if num[j:j+len(n3)]==n3:
            return self.isvalid(num, i, j, j+len(n3))
