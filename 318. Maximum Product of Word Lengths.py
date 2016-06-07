# timeout

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordsbin=[[0 for j in xrange(26)] for i in xrange(len(words))]
        for i in xrange(len(words)):
            for letter in words[i]:
                wordsbin[i][ord(letter)-ord('a')]+=1
        maxx=0
        for i in xrange(1,len(wordsbin)):
            for j in xrange(i):
                check=0
                for k in xrange(26):
                    if int(wordsbin[i][k])>0 and int(wordsbin[j][k])>0:
                        check=1
                        break
                if check==0:
                    maxx=max(maxx,len(words[i])*len(words[j]))
        return maxx
