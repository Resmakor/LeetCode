class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        for i in range(0, len(s) - 1, 2):
            output += s[i] + chr(ord(s[i]) + int(s[i + 1]))
        if len(s) % 2 == 1:
            return output + s[-1]
        return output
            