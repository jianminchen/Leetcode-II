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
        head=TreeNode(-1)
        head.right=root
        node=head
        
        while node.right:
            node=node.right
            if node.left:
                end=node.left
                while end.right:
                    end=end.right
                temp=node.right
                node.right=node.left
                node.left=None
                end.right=temp
