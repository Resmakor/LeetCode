class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) != 1:
            counter = 0
            while(num != 0):
                counter += num % 10
                num /= 10
            num = counter
        return num