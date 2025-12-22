class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2 or n == 3:
            return n
        a, b, c = 2, 3, 0
        for i in range(3, n):
            c = a + b
            a, b = b, c
        return c