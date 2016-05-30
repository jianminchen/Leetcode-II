# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root=TreeNode(preorder.pop(0))
            rootindex=inorder.index(root.val)
            root.left=self.buildTree(preorder,inorder[:rootindex])
            root.right=self.buildTree(preorder,inorder[rootindex+1:])
            return root
