import math
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                c = math.sqrt(i ** 2 + j ** 2)
                if c <= n and c == int(c):
                    output += 2
        return output