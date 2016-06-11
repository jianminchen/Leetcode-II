# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        cur=head
        while cur.next:
            if cur.val>cur.next.val:
                pre=dummy
                while pre.next.val<cur.next.val:
                    pre=pre.next
                curnext=cur.next
                cur.next=curnext.next
                curnext.next=pre.next
                pre.next=curnext
            else:
                cur=cur.next
        return dummy.next    
