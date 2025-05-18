
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a % b)
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = head
        while current_node and current_node.next:
            new_node = ListNode(self.gcd(current_node.val, current_node.next.val))
            temp_node = current_node.next
            current_node.next = new_node
            new_node.next = temp_node
            current_node = current_node.next.next
        return head



