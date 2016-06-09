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
                queue=[]
                res=[]
                check=0 # check whether the region is surrounded
                if board[i][j]==u"O" and visited[i][j]==False:
                    visited[i][j]=True
                    queue+=[(i,j)]
                while len(queue)>0:
                    current=queue.pop(0)
                    x, y=current[0], current[1]
                    not_boundary=0
                    if x-1>=0:
                        if board[x-1][y]==u"O" and visited[x-1][y]==False:
                            visited[x-1][y]=True
                            queue+=[(x-1,y)]
                        not_boundary+=1
                    if x+1<m:
                        if board[x+1][y]==u"O" and visited[x+1][y]==False:
                            visited[x+1][y]=True
                            queue+=[(x+1,y)]
                        not_boundary+=1
                    if y-1>=0:
                        if board[x][y-1]==u"O" and visited[x][y-1]==False:
                            visited[x][y-1]=True
                            queue+=[(x,y-1)]
                        not_boundary+=1
                    if y+1<n:
                        if board[x][y+1]==u"O" and visited[x][y+1]==False:
                            visited[x][y+1]=True
                            queue+=[(x,y+1)]
                        not_boundary+=1
                    if not_boundary==4:
                        res+=[(x,y)]
                    else:
                        check=1
                if check==0:
                    for l in res:
                        board[l[0]][l[1]]="X"
