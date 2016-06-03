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
        dic={}
        dummynode=ListNode(-1)
        dummynode.next=head
        pre=dummynode
        
        while head:
            if head.val not in dic:
                dic[head.val]=1
                head=head.next
                pre=pre.next
            else:
                temp=head.next
                pre.next=temp
                del head
                head=temp
            
        return dummynode.next
