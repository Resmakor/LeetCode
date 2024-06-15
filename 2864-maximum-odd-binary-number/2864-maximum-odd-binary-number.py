class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')
        zeros = len(s) - ones
        output = '1' * (ones - 1) + '0' * zeros + '1'
        return output
            
            