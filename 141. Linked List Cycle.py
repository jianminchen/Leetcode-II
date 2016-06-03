# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pfast=head
        pslow=head
        
        while pslow and pfast and pfast.next:
            pfast=pfast.next.next
            pslow=pslow.next
            if pfast==pslow:
                return True
        
        return False
