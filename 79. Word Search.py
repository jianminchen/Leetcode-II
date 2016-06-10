class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m=len(board)
        self.n=len(board[0])
        visited=[[False for j in xrange(self.n)] for i in xrange(self.m)]
        for i in xrange(self.m):
            for j in xrange(self.n):
                if self.DFS(0, i, j, board, word, visited):
                    return True
        return False
        
    def DFS(self, index, i, j, board, word, visited):
        if index==len(word):
            return True
        if i<0 or j<0 or i>self.m-1 or j>self.n-1 or visited[i][j] or word[index]!=board[i][j]:
            return False
        visited[i][j]=True
        res=self.DFS(index+1, i-1, j, board, word, visited) or self.DFS(index+1, i+1, j, board, word, visited) or self.DFS(index+1, i, j-1, board, word, visited) or self.DFS(index+1, i, j+1, board, word, visited)
        visited[i][j]=False
        return res
