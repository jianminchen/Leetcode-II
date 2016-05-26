# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        self.dic={}
        return self.gt(1,n)
    
    def gt(self,start,end):
        roots=[]
        for root in xrange(start,end+1):
            for left in self.gt(start,root-1):
                for right in self.gt(root+1,end):
                    if root not in self.dic:
                        node=TreeNode(root)
                        node.left=left
                        node.right=right
                        roots.append(node)
        self.dic[(start,end)]=roots
        return self.dic[(start,end)] or [None]
        
if __name__ == "__main__":
    None
