class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_sorted = sorted(list(str(n)))
        return int(n_sorted[-1]) * int(n_sorted[-2])