class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        counter = 0
        while True:
            if num1 == 0 or num2 == 0:
                return counter
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            counter += 1