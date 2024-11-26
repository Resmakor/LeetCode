class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i ** 2 for i in range(1, n + 1)]
        output = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                if i ** 2 + j ** 2 in squares:
                    output += 1
        return output * 2