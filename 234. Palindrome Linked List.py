# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findmid(self,head):
        pfast=head
        pslow=head
        while pfast:
            if pfast:
                pfast=pfast.next
                self.even=0
            if pfast:
                pfast=pfast.next
                pslow=pslow.next
                self.even=1
        return pslow
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        self.even=0
        mid=self.findmid(head)
        head2=mid
        dummy=ListNode(-1)
        nextnode=None
        
        while head and head!=head2:
            temp=ListNode(head.val)
            temp.next=nextnode
            dummy.next=temp
            nextnode=temp
            head=head.next
        if self.even==0 and head:
            temp=ListNode(head.val)
            temp.next=nextnode
            dummy.next=temp
            nextnode=temp
        head1=dummy.next
        
        while head1 and head2:
            if head1.val!=head2.val:
                return False
            head1=head1.next
            head2=head2.next
        return True
