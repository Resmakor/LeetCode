class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for element in s:
            if len(stack) > 0 and stack[-1] == element:
                stack.pop()
            else:
                stack.append(element)
        return ''.join(stack)
             