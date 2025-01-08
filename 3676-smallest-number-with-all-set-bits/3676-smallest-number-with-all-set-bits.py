class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_len = len(str(bin(n).lstrip('0b')))
        return int('1' * max_len, 2)