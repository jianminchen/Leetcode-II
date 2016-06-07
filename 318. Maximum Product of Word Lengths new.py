class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordsbin=[0 for i in xrange(len(words))]
        for i in xrange(len(words)):
            for letter in words[i]:
                wordsbin[i]|= 1 << (ord(letter)-97)
        maxx=0
        for i in xrange(1,len(wordsbin)):
            for j in xrange(i):
                if not (wordsbin[i] & wordsbin[j]):
                    maxx=max(maxx,len(words[i])*len(words[j]))
        return maxx
