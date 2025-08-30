class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n).lstrip('0b')[::-1]
        binary += '0' * (32 - len(binary))
        return int(binary, 2)