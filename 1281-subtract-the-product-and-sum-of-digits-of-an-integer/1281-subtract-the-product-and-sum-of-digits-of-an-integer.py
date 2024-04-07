class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_product = 1
        n_sum = 0
        for digit in str(n):
            n_product *= int(digit)
            n_sum += int(digit)
        return n_product - n_sum