class Solution(object):
    def digitProduct(self, n):
        number = 1
        for element in str(n):
            number *= int(element)
        return number
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            if self.digitProduct(n) % t == 0:
                return n
            else:
                n += 1