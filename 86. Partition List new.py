# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1 = ListNode(-1)
        less_than_x=dummy1
        dummy2 = ListNode(-1)
        not_less_than_x=dummy2
        
        while head:
            if head.val<x:
                less_than_x.next=head
                head=head.next
                less_than_x=less_than_x.next
                less_than_x.next=None
            else:
                not_less_than_x.next=head
                head=head.next
                not_less_than_x=not_less_than_x.next
                not_less_than_x.next=None
        
        less_than_x.next=dummy2.next
        return dummy1.next
