# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        while head and head.next:
            temp=head.next.next
            pre.next=head.next
            head.next.next=head
            head.next=temp
            head=pre.next
            head=head.next.next
            pre=pre.next.next
        return dummy.next
