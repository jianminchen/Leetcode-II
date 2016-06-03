# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummynode=ListNode(-1)
        dummynode.next=head
        pre=dummynode
        
        while head:
            if head.next and head.val==head.next.val:
                pre.next=head.next
                head=head.next
            else:
                pre=pre.next
                head=head.next
        return dummynode.next
