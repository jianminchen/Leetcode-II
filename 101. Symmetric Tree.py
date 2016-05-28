# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leftdfs(self,root):
        if root==None:
            self.left.append(None)
            return 
        self.left.append(root.val)
        self.leftdfs(root.left)
        self.leftdfs(root.right)
        
    def rightdfs(self,root):
        if root==None:
            self.right.append(None)
            return 
        self.right.append(root.val)
        self.rightdfs(root.right)
        self.rightdfs(root.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.left=[]
        self.right=[]
        self.leftdfs(root)
        self.rightdfs(root)
        if self.left==self.right:
            return True
        else:
            return False
        
