# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if root:
            self.dfs(root,res,0)
        return res
        
    def dfs(self,root,res,level):
        if root==None:
            return
        if level==len(res):
            res+=[root.val]
        self.dfs(root.right,res,level+1)
        self.dfs(root.left,res,level+1)
