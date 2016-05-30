# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        self.res=[]
        self.s=s
        self.path(root, [root.val])
        return self.res
    
    def path(self, root, pathlist):
        if root.left==None and root.right==None:
            if sum(pathlist)==self.s:
                self.res.append(pathlist)
            return
        else:
            if root.left:
                self.path(root.left, pathlist+[root.left.val])
            if root.right:
                self.path(root.right, pathlist+[root.right.val])
