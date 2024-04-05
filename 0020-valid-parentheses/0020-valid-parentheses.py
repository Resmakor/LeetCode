class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        if len(s) == 1:
            return 0
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(str(char))
                continue
            elif stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
                break
        return len(stack) == 0
        
                