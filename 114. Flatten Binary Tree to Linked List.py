# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        self.tlist=[]
        self.preorder(root)
        for i in xrange(len(self.tlist)-1):
            self.tlist[i].left=None
            self.tlist[i].right=self.tlist[i+1]
        
    def preorder(self, root):
        if root==None:
            return
        self.tlist+=[root]
        self.preorder(root.left)
        self.preorder(root.right)
