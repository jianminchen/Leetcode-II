# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        level=0
        queue=[(root,0)]
        res=[[]]
        while len(queue)>0:
            if queue[0][1]==level:
                temp=queue.pop(0)
                res[len(res)-1]+=[temp[0].val]
                if temp[0].left:
                    queue+=[(temp[0].left,level+1)]
                if temp[0].right:
                    queue+=[(temp[0].right,level+1)]
            else:
                if level%2!=0:
                    res[len(res)-1]=res[len(res)-1][::-1]
                level+=1
                res+=[[]]
        if level%2!=0:
            res[len(res)-1]=res[len(res)-1][::-1]
        return res
