# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        nextnode=None
        
        while head:
            temp=ListNode(head.val)
            temp.next=nextnode
            nextnode=temp
            dummy.next=temp
            pre=head
            head=head.next
            del pre
            
        return dummy.next
