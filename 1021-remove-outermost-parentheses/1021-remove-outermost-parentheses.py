class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        output, opened = "", 0
        for character in s:
            if character == ')':
                opened -= 1
            if opened != 0:
                output += character
            if character == '(':
                opened += 1
            
        return output
                
                
                