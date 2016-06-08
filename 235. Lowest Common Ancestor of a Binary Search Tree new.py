# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or p==None or q==None:
            return root
        res=root
        while res:
            if p.val>res.val and q.val>res.val:
                res=res.right
            elif p.val<res.val and q.val<res.val:
                res=res.left
            else:
                break
        return res
