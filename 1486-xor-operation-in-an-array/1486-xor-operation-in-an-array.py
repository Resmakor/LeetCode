class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        output = 0
        for i in range(n):
            output ^= start + 2 * i
        return output
        