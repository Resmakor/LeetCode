class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        a, b, c = 0, 1, 1
        for i in range(2, n):
            d = a + b + c
            a, b, c = b, c, d
        return c