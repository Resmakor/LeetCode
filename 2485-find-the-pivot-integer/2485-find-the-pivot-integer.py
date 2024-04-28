class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_list = list(range(1, n + 1))
        for i in range(1, n + 1):
            if sum(n_list[:i]) == sum(n_list[i - 1:]):
                return i
        return -1