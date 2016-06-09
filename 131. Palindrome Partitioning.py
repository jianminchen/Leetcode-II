class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res=[]
        self.DFS(s,[],0)
        return self.res
        
    def DFS(self, s, path, start):
        if start==len(s):
            self.res+=[path[:]]
            return
        for i in xrange(start,len(s)):
            temp=s[start:i+1]
            if temp!="" and self.palindrome(temp):
                path+=[temp]
                self.DFS(s, path, i+1)
                path.pop()
        
    def palindrome(self, s):
        for i in xrange(len(s)/2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
