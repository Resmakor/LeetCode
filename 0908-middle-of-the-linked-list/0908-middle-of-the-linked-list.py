# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counter, temp = 0, head
        while temp != None:
            counter += 1
            temp = temp.next
        center = counter // 2
        temp = head
        while center > 0:
            temp = temp.next
            center -= 1
        return temp