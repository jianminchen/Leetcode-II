class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        return self.DFS(grid)
        
    def DFS(self, grid):
        m=len(grid)
        n=len(grid[0])
        visited=[[False for j in xrange(n)] for i in xrange(m)]
        island=0
        for i in xrange(m):
            for j in xrange(n):
                stack=[]
                if grid[i][j]=='1' and visited[i][j]==False:
                    visited[i][j]=True
                    stack+=[(i,j)]
                    island+=1
                while len(stack)>0:
                    current=stack.pop()
                    x, y=current[0], current[1]
                    if x-1>=0 and grid[x-1][y]=='1' and visited[x-1][y]==False:
                        visited[x-1][y]=True
                        stack+=[(x-1,y)]
                    if x+1<m and grid[x+1][y]=='1' and visited[x+1][y]==False:
                        visited[x+1][y]=True
                        stack+=[(x+1,y)]
                    if y-1>=0 and grid[x][y-1]=='1' and visited[x][y-1]==False:
                        visited[x][y-1]=True
                        stack+=[(x,y-1)]
                    if y+1<n and grid[x][y+1]=='1' and visited[x][y+1]==False:
                        visited[x][y+1]=True
                        stack+=[(x,y+1)]
        return island
