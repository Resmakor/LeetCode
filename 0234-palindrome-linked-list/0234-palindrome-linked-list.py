# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        for i in range(len(stack)):
            if stack[i] != stack[len(stack) - i - 1]:
                return False
        return True