# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        dummy.next=head
        pfast=head
        pslow=head
        
        if head.next==None and n==1:
            return []
            
        for i in xrange(n):
            pfast=pfast.next
            
        while pfast:
            if n>1:
                pfast=pfast.next
                pslow=pslow.next
            elif n==1:
                pfast=pfast.next
                if pfast:
                    pslow=pslow.next
        if n>1:
            if pslow.next:
                pslow.val=pslow.next.val
                pslow.next=pslow.next.next
        else:
            pslow.next=None
        
        return head
