class Solution(object):  
    def compareVersion(self, version1, version2):  
        """ 
        :type version1: str 
        :type version2: str 
        :rtype: int 
        """  
        v1=version1.split('.')  
        v2=version2.split('.')
        
        while len(v1)<len(v2):  
            v1.append('0')  
        while len(v1)>len(v2):  
            v2.append('0')  
        for i,j in zip(v1,v2):  
            if int(i)>int(j):
                return 1  
            if int(i)<int(j):
                return -1  
        return 0  
