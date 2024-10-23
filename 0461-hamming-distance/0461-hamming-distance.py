class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        output = 0
        x, y = bin(x).lstrip('0b'), bin(y).lstrip('0b')
        if len(x) > len(y):
            y = '0' * (len(x) - len(y)) + y
        elif len(y) > len(x):
            x = '0' * (len(y) - len(x)) + x
        for i in range(len(x)):
            if x[i] != y[i]:
                output += 1
        return output