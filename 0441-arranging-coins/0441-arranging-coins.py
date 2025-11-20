class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(-0.5 + (sqrt(8 * n + 1) / 2))