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
        pre=dummy
        p=head
        
        length=0
        while p:
            length+=1
            p=p.next

        while head:
            if length==n:
                pre.next=head.next
                head=head.next
            else:
                pre=pre.next
                head=head.next
            length-=1
        
        return dummy.next
