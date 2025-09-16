class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        output = 0
        for letter in columnTitle:
            output = output * 26 + ord(letter) - 64
        return output