class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        i = 0
        while n:
            d = n % 10
            if d:
                output.append(d * 10 ** i)
            i += 1
            n //= 10
        return output[::-1]