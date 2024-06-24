class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        output = ""
        for word in s:
            output += word[::-1] + ' '
        return output[:-1]