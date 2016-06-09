class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)>0:
            self.DFS(board)
    
    def DFS(self, board):
        m=len(board)
        n=len(board[0])
        visited=[[False for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                stack=[]
                res=[]
                check=0 # check whether the region is surrounded
                if board[i][j]==u"O" and visited[i][j]==False:
                    visited[i][j]=True
                    stack+=[(i,j)]
                while len(stack)>0:
                    current=stack.pop()
                    x, y=current[0], current[1]
                    not_boundary=0
                    if x-1>=0:
                        if board[x-1][y]==u"O" and visited[x-1][y]==False:
                            visited[x-1][y]=True
                            stack+=[(x-1,y)]
                        not_boundary+=1
                    if x+1<m:
                        if board[x+1][y]==u"O" and visited[x+1][y]==False:
                            visited[x+1][y]=True
                            stack+=[(x+1,y)]
                        not_boundary+=1
                    if y-1>=0:
                        if board[x][y-1]==u"O" and visited[x][y-1]==False:
                            visited[x][y-1]=True
                            stack+=[(x,y-1)]
                        not_boundary+=1
                    if y+1<n:
                        if board[x][y+1]==u"O" and visited[x][y+1]==False:
                            visited[x][y+1]=True
                            stack+=[(x,y+1)]
                        not_boundary+=1
                    if not_boundary==4:
                        res+=[(x,y)]
                    else:
                        check=1
                if check==0:
                    for l in res:
                        board[l[0]][l[1]]="X"
