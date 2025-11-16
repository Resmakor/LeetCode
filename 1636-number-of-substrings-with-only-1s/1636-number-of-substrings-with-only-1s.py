class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split('0')
        mod = 1000000007
        output = 0
        for substring in s:
            size = len(substring)
            output += (size * (size + 1) / 2) % mod
        return output