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
        check=0
        # node "pre" and node "head" have different values
        while head and head.next:
            while head.next and head.val==head.next.val:
                head=head.next
                check+=1
            head=head.next
            if check==0:
                pre=pre.next
            else:
                pre.next=head
            check=0
        return dummynode.next
