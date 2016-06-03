class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b=map(int,list(a)), map(int,list(b))
        p1, p2=len(a)-1, len(b)-1
        en=0
        res=[]
        
        while p1>=0 and p2>=0:
            if a[p1]+b[p2]+en<2:
                res+=[a[p1]+b[p2]+en]
                en=0
            else:
                res+=[a[p1]+b[p2]+en-2]
                en=1
            p1-=1
            p2-=1
            
        while p1>=0:
            if a[p1]+en<2:
                res+=[a[p1]+en]
                en=0
            else:
                res+=[a[p1]+en-2]
                en=1
            p1-=1
        
        while p2>=0:
            if b[p2]+en<2:
                res+=[b[p2]+en]
                en=0
            else:
                res+=[b[p2]+en-2]
                en=1
            p2-=1
        
        if en==1:
            res+=[en]
            
        return "".join(str(i) for i in res[::-1])
