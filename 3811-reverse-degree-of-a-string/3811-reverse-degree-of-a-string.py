class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        for index, char in enumerate(s):
            output += (index + 1) * (27 - ord(char) + 96)
        return output