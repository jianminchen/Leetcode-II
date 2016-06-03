# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(-1)
        pre=head
        
        while l1 and l2:
            if l1.val<l2.val:
                node=ListNode(l1.val)
                pre.next=node
                if l1:
                    l1=l1.next
            else:
                node=ListNode(l2.val)
                pre.next=node
                if l2:
                    l2=l2.next
            pre=pre.next
        
        while l1:
            node=ListNode(l1.val)
            pre.next=node
            if l1:
                l1=l1.next
            pre=pre.next
        
        while l2:
            node=ListNode(l2.val)
            pre.next=node
            if l2:
                l2=l2.next
            pre=pre.next
            
        return head.next
