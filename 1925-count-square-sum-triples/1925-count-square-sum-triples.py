class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_sq = a * a + b * b
                c = int(sqrt(c_sq))
                if c * c == c_sq and c <= n:
                    output += 1
        return output