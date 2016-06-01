class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        self.matrix=matrix
        self.path=[]
        self.sprial(0, 0, 1, len(matrix)-1, 0, len(matrix[0])-1,'R')
        return self.path
        
    def sprial(self, x, y, u, d, l, r, direction):
        
        if len(self.path)<len(self.matrix)*len(self.matrix[0]):
            self.path+=[self.matrix[y][x]]
        else:
            return
        
        if direction=="R":
            if x+1>r:
                direction = "D"
                r-=1
                self.sprial(x, y+1, u, d, l, r, direction)
            else:
                self.sprial(x+1, y, u, d, l, r, direction)
        elif direction=="D":
            if y+1>d:
                direction = "L"
                d-=1
                self.sprial(x-1, y, u, d, l, r, direction)
            else:
                self.sprial(x, y+1, u, d, l, r, direction)
        elif direction=="L":
            if x-1<l:
                direction = "U"
                l+=1
                self.sprial(x, y-1, u, d, l, r, direction)
            else:
                self.sprial(x-1, y, u, d, l, r, direction)
        elif direction=="U":
            if y-1<u:
                direction = "R"
                u+=1
                self.sprial(x+1, y, u, d, l, r, direction)
            else:
                self.sprial(x, y-1, u, d, l, r, direction)
