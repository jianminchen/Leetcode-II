# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        en=0
        head=ListNode(-1)
        prev=head
        while l1 and l2:
            if l1.val+l2.val+en<10:
                node=ListNode(l1.val+l2.val+en)
                en=0
                prev.next=node
            else:
                node=ListNode(l1.val+l2.val+en-10)
                en=1
                prev.next=node
            l1=l1.next
            l2=l2.next
            prev=prev.next
            
        while l1:
            if l1.val+en<10:
                node=ListNode(l1.val+en)
                en=0
                prev.next=node
            else:
                node=ListNode(l1.val+en-10)
                en=1
                prev.next=node
            l1=l1.next
            prev=prev.next
            
        while l2:
            if l2.val+en<10:
                node=ListNode(l2.val+en)
                en=0
                prev.next=node
            else:
                node=ListNode(l2.val+en-10)
                en=1
                prev.next=node
            l2=l2.next
            prev=prev.next
            
        if en==1:
            node=ListNode(en)
            prev.next=node
            
        return head.next
