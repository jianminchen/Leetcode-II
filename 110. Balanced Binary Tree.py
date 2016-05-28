# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.depth(root)!=-1
    
    def depth(self,root):
        if root==None:
            return True
        left=self.depth(root.left)
        if left==-1:
            return -1
        right=self.depth(root.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return max(left,right)+1
