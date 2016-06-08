# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
            return None
        self.k=k
        self.res=0
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if root==None:
            return
        self.dfs(root.left)
        self.k-=1
        if self.k==0:
            self.res=root.val
            return
        self.dfs(root.right)
