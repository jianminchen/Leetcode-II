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
        self.res_sum=0
        if root==None:
            return 0
        self.sum(root,root.val)
        return self.res_sum
        
    def sum(self,root,res):
        if root.left==None and root.right==None:
            self.res_sum+=res
            return
        else:
            if root.left:
                self.sum(root.left,10*res+root.left.val)
            if root.right:
                self.sum(root.right,10*res+root.right.val)
