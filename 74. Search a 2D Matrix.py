class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if row[0]<=target and row[len(row)-1]>=target:
                if target in row:
                    return True
        return False
