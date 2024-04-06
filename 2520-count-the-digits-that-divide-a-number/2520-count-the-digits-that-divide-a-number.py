class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter = 0
        for digit in str(num):
            if num % int(digit) == 0:
                counter += 1
        return counter