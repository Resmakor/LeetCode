class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(bin(n).lstrip('0b'))
        n_reversed = n[::-1]
        output = 0
        for i in range(len(n)):
            if n[i] != n_reversed[i]:
                output += 1
        return output