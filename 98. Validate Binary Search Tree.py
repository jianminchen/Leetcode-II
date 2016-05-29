# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #The in-order sequence of a BST is increasing
        
        if root==None:
            return True
        self.inorder_list=[]
        self.inorder(root)
        for i in xrange(1,len(self.inorder_list)):
            if self.inorder_list[i]<=self.inorder_list[i-1]:
                return False
        return True
    
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        self.inorder_list.append(root.val)
        if root.right!=None:
            self.inorder(root.right)
