# timeout

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.adv={}
        visited={}
        self.tickets=tickets
        for i in tickets:
            if i[0] not in self.adv:
                self.adv[i[0]]=[]
                visited[i[0]]=[]
            self.adv[i[0]]+=[i[1]]
            visited[i[0]]+=[False]
        for key, value in self.adv.iteritems():
            self.adv[key]=sorted(value)
        for i, j in self.adv.iteritems():
            self.res=""
            self.DFS([i], visited)
            if self.res!="":
                return self.res
            
    def DFS(self, path, visited):
        if len(path)==len(self.tickets)+1:
            self.res=path[:]
            return
        if path[len(path)-1] in self.adv and path[len(path)-1] in visited:
            if len(path)<len(self.tickets):
                for i in xrange(len(self.adv[path[len(path)-1]])):
                    if self.adv[path[len(path)-1]][i] in visited and visited[path[len(path)-1]][i]==False:
                        visited[path[len(path)-1]][i]=True
                        path+=[self.adv[path[len(path)-1]][i]]
                        self.DFS(path, visited)
                        if self.res!="":
                            break
                        path.pop()
                        visited[path[len(path)-1]][i]=False
            elif len(path)==len(self.tickets):
                for i in xrange(len(self.adv[path[len(path)-1]])):
                    if visited[path[len(path)-1]][i]==False:
                        visited[path[len(path)-1]][i]=True
                        path+=[self.adv[path[len(path)-1]][i]]
                        self.DFS(path, visited)
                        if self.res!="":
                            break
                        path.pop()
                        visited[path[len(path)-1]][i]=False
        return
