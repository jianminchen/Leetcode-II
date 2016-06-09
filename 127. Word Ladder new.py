import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        visited=set()
        queue=[]        
        visited.add(beginWord)
        queue+=[beginWord]
        distance={}
        distance[beginWord]=1
        while len(queue)>0:
            current=queue.pop(0)
            for i in self.getNextWord(current, wordList):
                if i in visited:
                    continue
                visited.add(i)
                queue+=[i]
                distance[i]=distance[current]+1
                if i==endWord:
                    return distance[i]
        return 0
    
    def getNextWord(self, word, dict):
        aToz=string.ascii_lowercase
        res=[]
        for char in aToz:
            for j in range(len(word)):
                if word[j]==char:
                    continue
                newWord=word[:j]+char+word[j+1:]
                if newWord in dict:
                    res.append(newWord)
        return res  
