# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        str_bin = str(head.val)
        while head.next != None:
            head = head.next
            str_bin += str(head.val)
        return int(str_bin, 2)