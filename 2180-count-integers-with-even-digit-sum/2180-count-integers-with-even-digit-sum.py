class Solution(object):
    def evenDigitSum(self, num):
        """
        :type num: int
        :rtype: bool
        """
        output = 0
        while num != 0:
            output += num % 10
            num //= 10
        return output % 2 == 0
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = 0
        for i in range(1, num + 1):
            if self.evenDigitSum(i):
                output += 1
        return output