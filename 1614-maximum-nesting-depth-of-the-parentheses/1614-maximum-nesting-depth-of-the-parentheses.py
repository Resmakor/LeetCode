class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        maximum = 0
        for character in s:
            if character == ')':
                counter -= 1
            elif character == '(':
                counter += 1
            if counter > maximum:
                maximum = counter
        return maximum
                