class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4 or len(s)>12:
            return []
        self.res=[]
        self.DFS(s,[],0)
        return self.res
        
    def DFS(self, s, path, start):
        if start==len(s) and len(path)==4:
            self.res+=[".".join(path)]
            return
        for i in xrange(start,len(s)):
            temp=s[start:i+1]
            if (len(temp)==1 or (len(temp)>1 and temp[0]!="0")) and int(temp)>=0 and int(temp)<=255:
                path+=[temp]
                self.DFS(s,path,i+1)
                path.pop()
