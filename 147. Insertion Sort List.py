# timeout

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
        prep1=dummy
        p1=head
        p2=head.next
        while p2!=None:
            if p2.val<p1.val:
                while p1.next!=p2:
                    p1=p1.next
                p1.next=p2.next
                p2.next=prep1.next
                prep1.next=p2
                p2=p1.next
                p1=dummy.next
                prep1=dummy
            else:
                if p1!=p2:
                    p1=p1.next
                    prep1=prep1.next
                else:
                    p1=dummy.next
                    prep1=dummy
                    p2=p2.next
        return dummy.next
