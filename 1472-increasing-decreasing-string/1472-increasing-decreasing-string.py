from collections import Counter

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        s = list(s)
        while s:
            for letter in sorted(set(s)):
                s.remove(letter)
                output += letter
            for letter in sorted(set(s), reverse=True):
                s.remove(letter)
                output += letter
        return output