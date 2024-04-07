class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_product = 1
        n_sum = 0
        while n != 0:
            digit = n % 10
            n //= 10
            n_product *= digit
            n_sum += digit
        return n_product - n_sum