class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible = 0
        not_divisible = 0
        for i in range(1, n + 1):
            if i % m == 0:
                divisible += i
            else:
                not_divisible += i
        return not_divisible - divisible
            