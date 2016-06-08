# BFS, timeout

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.adj=[[0 for j in xrange(n)] for i in xrange(n)]
        self.n=n
        for i in edges:
            self.adj[i[0]][i[1]]=1
            self.adj[i[1]][i[0]]=1
        return self.BFS()
    
    def BFS(self):
        minn=self.n
        res=[]
        for root in xrange(self.n):
            visited=[False for i in xrange(self.n)]
            queue=[]
            distance=[0 for i in xrange(self.n)]
            visited[root]=True
            queue+=[root]
            while len(queue)>0:
                current=queue.pop()
                for i in xrange(self.n):
                    if self.adj[current][i]==1 and visited[i]==False:
                        visited[i]=True
                        queue+=[i]
                        distance[i]=distance[current]+1
                        temp=distance[i]
            temp=max(distance)
            if temp<minn:
                minn=temp
                res=[root]
            elif temp==minn:
                res+=[root]
        return res
