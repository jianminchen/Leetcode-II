# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy=root
        self.dfs(root)
        return dummy
        
    def dfs(self, root):
        if root:
            temp=root.right
            root.right=root.left
            root.left=temp
            self.dfs(root.left)
            self.dfs(root.right)
