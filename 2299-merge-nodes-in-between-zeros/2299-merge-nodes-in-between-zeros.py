# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(0, None)
        temp_head = new_head
        while head.next != None:
            while head.next.val != 0:
                new_head.val += head.next.val
                head = head.next
            else:
                if head.next.next != None:
                    new_head.next = ListNode(0, None)
                    new_head = new_head.next
                head = head.next
        return temp_head