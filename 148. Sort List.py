# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p1=head
        p2=head.next
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
        p2=self.sortList(p1.next)
        p1.next=None
        p1=self.sortList(head)
        return self.merge(p1, p2)

    def merge(self, p1, p2):
        dummy=ListNode(-1)
        p=dummy
        while p1 and p2:
            if p1.val<p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next
            p=p.next
        if p1:
            p.next=p1
        else:
            p.next=p2
        return dummy.next
