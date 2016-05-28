# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.isSameTree(root.left,root.right)
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        elif (p==None and q!=None) or (p!=None and q==None):
            return False
        elif (p!=None and q!=None) and p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
