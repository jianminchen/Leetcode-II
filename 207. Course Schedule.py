# detect cycle in a undirected graph
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited=[False for i in xrange(numCourses)]
        recstack=[False for i in xrange(numCourses)]
        adj=[[] for i in xrange(numCourses)]
        for i in prerequisites:
            adj[i[1]]+=[i[0]]
        for i in xrange(numCourses):
            if self.cycle_exist(i, visited, recstack, adj):
                return False
        return True
            
    def cycle_exist(self, node, visited, recstack, adj):
        if visited[node]==False:
            visited[node]=True
            recstack[node]=True
            for i in adj[node]:
                if visited[i]==False and self.cycle_exist(i, visited, recstack, adj):
                    return True
                elif recstack[i]:
                    return True
        recstack[node]=False
        return False
