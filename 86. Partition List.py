# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        dummy.next=head
        end_of_less_than_x=dummy
        head_of_not_less_than_x=None
        end_of_not_less_than_x=None
        
        while head:
            if head.val<x:
                if head_of_not_less_than_x:
                    end_of_not_less_than_x.next=head.next
                    if end_of_not_less_than_x:
                        head.next=head_of_not_less_than_x
                        end_of_less_than_x.next=head
                        end_of_less_than_x=head
                        head=end_of_not_less_than_x.next
                    else:
                        end_of_less_than_x.next=head
                        head.next=head_of_not_less_than_x
                else:
                    end_of_less_than_x=head
                    head=head.next
            else:
                if head_of_not_less_than_x:
                    end_of_not_less_than_x=head
                    head=head.next
                else:
                    head_of_not_less_than_x=head
                    
        return dummy.next
