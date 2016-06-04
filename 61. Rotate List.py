# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or head==None:
            return head
            
        length=0
        p=head
        while p.next:
            length+=1
            p=p.next
        length+=1
        p.next=head # connect the head and tail of the list
        
        if k>length:
            k=k%length
        while length>k: # rotate and break the loop
            p=p.next
            length-=1
            
        res=p.next
        p.next=None
        return res
