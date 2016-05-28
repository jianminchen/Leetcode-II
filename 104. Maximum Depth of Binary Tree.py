# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        root.val=1
        self.dep=0
        self.depth(root)
        return self.dep
        
    # save the depth of each node into each node's val
    def depth(self,root):
        if root.left==None and root.right==None: #leaf
            self.dep=max(root.val,self.dep)
            return
        else: #not leaf
            if root.left!=None:
                root.left.val=root.val+1
                self.depth(root.left)
            if root.right!=None:
                root.right.val=root.val+1
                self.depth(root.right)
