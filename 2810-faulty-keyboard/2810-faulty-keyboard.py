class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        for character in s:
            if character == 'i':
                output = output[::-1]
            else:
                output += character
        return output