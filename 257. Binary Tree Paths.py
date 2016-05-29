# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root==None:
            return []
        self.res=[]
        self.path(root,str(root.val))
        return self.res
        
    def path(self,root,pstr):
        if root.left==None and root.right==None:
            self.res.append(pstr)
            return
        else:
            if root.left:
                self.path(root.left,pstr+"->"+str(root.left.val))
            if root.right:
                self.path(root.right,pstr+"->"+str(root.right.val))
