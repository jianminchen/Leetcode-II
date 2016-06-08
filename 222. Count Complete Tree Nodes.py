# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l=self.leftheight(root)+1
        r=self.rightheight(root)+1
        if l==r:
            return 2**(l-1)-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1
        
    def leftheight(self, root):
        height=0
        while root:
            height+=1
            root=root.left
        return height
    
    def rightheight(self, root):
        height=0
        while root:
            height+=1
            root=root.right
        return height
