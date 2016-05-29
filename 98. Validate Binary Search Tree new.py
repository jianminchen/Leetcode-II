# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        if root.left and root.val<=self.lmax(root.left):
            return False
        if root.right and root.val>=self.rmin(root.right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def lmax(self,root):
        if root==None:
            return -sys.maxint
        return max(root.val, self.lmax(root.left), self.lmax(root.right))
    
    def rmin(self,root):
        if root==None:
            return sys.maxint
        return min(root.val, self.rmin(root.left), self.rmin(root.right))
