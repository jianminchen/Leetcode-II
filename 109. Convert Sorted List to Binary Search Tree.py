# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.numlist=[]
        while head!=None:
            self.numlist.append(head.val)
            head=head.next
        return self.sortedArrayToBST(self.numlist)
            
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n=len(nums)
        if n==0:
            return None
        mid=n/2
        node=TreeNode(nums[mid])
        node.left=self.sortedArrayToBST(nums[:mid])
        node.right=self.sortedArrayToBST(nums[mid+1:])
        return node
