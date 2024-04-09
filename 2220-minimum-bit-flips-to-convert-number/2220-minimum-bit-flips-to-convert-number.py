class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        xor = start ^ goal
        xor_bin = bin(xor).strip('0b')
        counter = 0
        for digit in xor_bin:
            if digit == '1':
                counter += 1
        return counter