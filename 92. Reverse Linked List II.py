# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res=ListNode(-1)
        res.next=head
        begin=res # begin: node m-1
        p=head
        i=1
        while i<m:
            if i==m-1:
                begin=p
            p=p.next
            i+=1
        dummy=ListNode(-1)
        nextnode=None
        end=None # end: node n
        while i<=n:
            temp=ListNode(p.val)
            if nextnode==None:
                end=temp
            temp.next=nextnode
            dummy.next=temp
            nextnode=temp
            p=p.next
            n-=1
        if begin:
            begin.next=dummy.next
        if end:
            end.next=p
        return res.next
