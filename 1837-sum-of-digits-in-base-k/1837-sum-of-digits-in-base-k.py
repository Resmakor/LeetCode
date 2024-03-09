class Solution(object):
    def convert(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        new_Base = ""
        while n != 0:
            new_Base += str(n % k)
            n //= k
        return new_Base
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        new_Base = self.convert(n, k)
        sum = 0
        for digit in new_Base:
            sum += int(digit)
        return sum