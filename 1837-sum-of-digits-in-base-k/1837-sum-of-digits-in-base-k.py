class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        new_Base_sum = 0
        while n != 0:
            new_Base_sum += n % k
            n //= k
        return new_Base_sum