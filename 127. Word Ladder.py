# BFS, timeout

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList=list(wordList)
        wordList.insert(0,beginWord)
        wordList.append(endWord)
        n=len(wordList)
        self.adj=[[0 for j in xrange(n)] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(i+1,n):
                diff=0
                for c1, c2 in zip(wordList[i],wordList[j]):
                    if c1!=c2:
                        diff+=1
                if diff==1:
                    self.adj[i][j]=1
                    self.adj[j][i]=1
        return self.BFS(n)
                    
    def BFS(self, n):
        visited=[False for i in xrange(n)]
        queue=[]
        distance=[1 for i in xrange(n)]
        
        visited[0]=True
        queue+=[0]
        while len(queue)>0:
            current=queue.pop()
            for i in xrange(1,n):
                if visited[i]==False and self.adj[current][i]==1:
                    visited[i]=True
                    queue+=[i]
                    distance[i]=distance[current]+1
        return distance[n-1]
