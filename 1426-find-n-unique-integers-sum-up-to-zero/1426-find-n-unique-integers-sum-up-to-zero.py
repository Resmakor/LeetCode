class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(1, (n // 2) + 1):
            output.extend([i, -i])
        if n % 2 != 0:
            return output + [0]
        return output