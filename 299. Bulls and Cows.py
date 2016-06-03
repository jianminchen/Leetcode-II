class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A={}
        dic={}
        num_of_B=0
        for i in xrange(len(secret)):
            if secret[i]==guess[i]:
                A[i]=1
            else:
                if secret[i] not in dic:
                    dic[secret[i]]=0
                dic[secret[i]]+=1
        
        for i in xrange(len(guess)):
            if i not in A and guess[i] in dic:
                if dic[guess[i]]>0:
                    num_of_B+=1
                    dic[guess[i]]-=1
        
        return str(len(A))+"A"+str(num_of_B)+"B"
