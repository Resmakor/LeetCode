class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        log_base = 4
        precision = 12
        return round(math.log(n, log_base), precision).is_integer()