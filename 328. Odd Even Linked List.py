# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        end_of_odd_group=dummy
        head_of_list=1
        index=1
        
        while head:
            if index % 2 != 0:
                pre.next=head.next
                if head_of_list:
                    pre=head
                else:
                    head.next=end_of_odd_group.next
                end_of_odd_group.next=head
                end_of_odd_group=end_of_odd_group.next
                head=pre.next
                head_of_list=0
            else:
                head=head.next
                pre=pre.next
            index+=1
            
        return dummy.next
