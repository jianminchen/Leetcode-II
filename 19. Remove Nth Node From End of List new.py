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
        p=head
        length=0
        
        while p:
            length+=1
            p=p.next
        if length==1 and n==1:
            return []
            
        while head:
            if n>1:
                if length==n:
                    if head.next:
                        head.val=head.next.val
                        head.next=head.next.next
                else:
                    head=head.next
            else:
                if length==2:
                    head.next=None
                else:
                    head=head.next
            length-=1
        
        return dummy.next
