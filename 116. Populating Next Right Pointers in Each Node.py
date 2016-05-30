# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            self.next(root)
        
    def next(self,root):
        if root.left==None and root.right==None:
            return
        else:
            if root.left:
                root.left.next=root.right
                self.next(root.left)
            if root.right:
                if root.next:
                    root.right.next=root.next.left
                self.next(root.right)
