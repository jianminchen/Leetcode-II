# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        self.check=0
        self.path(root,sum)
        if self.check==1:
            return True
        else:
            return False
        
    def path(self,root,sum):
        if root.left==None and root.right==None:
            if root.val==sum:
                self.check=1
                return
            else:
                return
        else:
            if root.left!=None:
                root.left.val+=root.val
                self.path(root.left,sum)
            if root.right!=None:
                root.right.val+=root.val
                self.path(root.right,sum)
