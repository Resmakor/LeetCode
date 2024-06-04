class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(1, n // 2 + 1):
            output.append(i)
            output.append(i * (-1))
        if n % 2 == 1:
            output.append(0)
        return output