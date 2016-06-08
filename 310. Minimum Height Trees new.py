class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        degree=[[] for x in range(n)]
        for i, j in edges:
            degree[i]+=[j]
            degree[j]+=[i]
        leaves=[i for i in range(n) if len(degree[i])<=1]
        while n>2:
            temp=[]
            n-=len(leaves)
            for i in leaves:
                for j in degree[i]:
                    degree[j].remove(i)
                    if len(degree[j])==1:
                        temp+=[j]
            leaves=temp
        return leaves
