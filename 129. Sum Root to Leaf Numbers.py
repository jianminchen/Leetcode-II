# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        self.res=0
        self.sum(root)
        return self.res
        
    def sum(self,root):
        if root.left==None and root.right==None:
            self.res+=root.val
            return
        else:
            if root.left:
                root.left.val+=10*root.val
                self.sum(root.left)
            if root.right:
                root.right.val+=10*root.val
                self.sum(root.right)
