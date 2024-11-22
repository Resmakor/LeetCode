class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        for i in range(len(s) - 1):
            value = s[0:i + 1].count('0') + s[i + 1:].count('1')
            if value > output:
                output = value
        return output