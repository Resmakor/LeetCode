class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible = []
        not_divisible = []
        for i in range(1, n + 1):
            if i % m == 0:
                divisible.append(i)
            else:
                not_divisible.append(i)
        return sum(not_divisible) - sum(divisible)
            