# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:  
            slow=head
            fast=head
            while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next

            head2=slow.next  
            slow.next=None
            dummy=ListNode(-1) 
            dummy.next=head2  
            p=head2.next  
            head2.next=None  
            while p:  
                temp=p  
                p=p.next  
                temp.next=dummy.next  
                dummy.next=temp
          
            p1=head  
            p2=dummy.next 
            while p2:  
                temp1=p1.next  
                p1.next=p2  
                temp2=p2.next  
                p2.next=temp1  
                p1=temp1  
                p2=temp2
