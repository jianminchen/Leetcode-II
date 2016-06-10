# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.DFS(root)[0]
        
    def DFS(self, root):
        if root==None:
            return 0, 0
        rL, nrL=self.DFS(root.left)
        rR, nrR=self.DFS(root.right)
        return max(rL+rR, nrL+nrR+root.val), rL+rR
