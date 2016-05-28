# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        return self.depth(root)
        
    def depth(self, root):
        if root==None:
            return 0
        left=self.depth(root.left)
        right=self.depth(root.right)
        if left==0 and right!=0:
            return right+1
        elif left!=0 and right==0:
            return left+1
        else:
            return min(left,right)+1
        if left==0 and right!=0:
            return right+1
        elif left!=0 and right==0:
            return left+1
        else:
            return min(left,right)+1
