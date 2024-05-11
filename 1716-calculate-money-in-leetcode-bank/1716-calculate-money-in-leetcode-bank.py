class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        dollars = 1
        while n > 0:
            for i in range(n if n < 7 else 7):
                output += i + dollars
            dollars += 1
            n -= 7
        return output
            