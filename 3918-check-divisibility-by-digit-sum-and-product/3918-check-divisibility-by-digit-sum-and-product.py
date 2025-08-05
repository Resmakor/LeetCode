class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit_sum, digit_product = 0, 1
        for element in str(n):
            digit_sum += int(element)
            digit_product *= int(element)
        return n % (digit_sum + digit_product) == 0