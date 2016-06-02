# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.traversal(root)
        return self.res
        
    def traversal(self, root):
        if root==None:
            return
        self.traversal(root.left)
        self.res+=[root.val]
        self.traversal(root.right)
        
