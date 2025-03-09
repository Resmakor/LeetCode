class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        div = k // (n - 1)
        mod = k % (n - 1)
        if div % 2 == 1:
            return (n - 1) - mod
        return mod