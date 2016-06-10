class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited=[False for i in xrange(numCourses)]
        recstack=[False for i in xrange(numCourses)]
        adj=[[] for i in xrange(numCourses)]
        self.res=[]
        for i in prerequisites:
            adj[i[1]]+=[i[0]]
        for i in xrange(numCourses):
            if self.cycle_exist(i, visited, recstack, adj):
                return []
        return self.res[::-1]
            
    def cycle_exist(self, node, visited, recstack, adj):
        if visited[node]==False:
            visited[node]=True
            recstack[node]=True
            for i in adj[node]:
                if visited[i]==False and self.cycle_exist(i, visited, recstack, adj):
                    return True
                elif recstack[i]:
                    return True
            self.res+=[node]
        recstack[node]=False
        return False
