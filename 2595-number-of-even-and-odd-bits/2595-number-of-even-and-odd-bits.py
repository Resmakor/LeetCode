class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        n = bin(n)[2:]
        output = [0, 0]
        for index, element in enumerate(n[::-1]):
            if element == '1':
                if index % 2 == 0:
                    output[0] += 1
                else:
                    output[1] += 1
        return output