# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res=[[root.val]]
        queue=[]
        level=0
        while True:
            if root.left:
                queue+=[[level+1, root.left]]
            if root.right:
                queue+=[[level+1, root.right]]
            if len(queue)==0:
                break
            current=queue.pop(0)
            root=current[1]
            if current[0]==len(res):
                res+=[[]]
                level+=1
            res[len(res)-1]+=[root.val]
        return res[::-1]
