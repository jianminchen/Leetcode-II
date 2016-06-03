# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA=0
        lengthB=0
        pA=headA
        pB=headB
        
        while pA:
            lengthA+=1
            pA=pA.next
        while pB:
            lengthB+=1
            pB=pB.next
        
        pA=headA
        pB=headB
        
        for i in xrange(lengthA-lengthB):
            pA=pA.next
        for i in xrange(lengthB-lengthA):
            pB=pB.next
        
        while pA and pB:
            if pA==pB:
                return pA
            pA=pA.next
            pB=pB.next
        
        return None
