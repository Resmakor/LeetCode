class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        xor_bin = bin(start ^ goal).strip('0b')
        counter = 0
        for digit in xor_bin:
            if digit == '1':
                counter += 1
        return counter