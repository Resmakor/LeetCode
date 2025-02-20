import math
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = i = 0
        while i < len(s):
            if s[i] == 'X':
                output += 1
                i += 3
            else:
                i += 1
        return output