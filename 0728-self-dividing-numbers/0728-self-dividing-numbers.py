class Solution(object):
    def selfDividingCheck(self, number):
        beginning = number
        while (number != 0):
            if number % 10 == 0:
                return False
            if beginning % (number % 10) != 0:
                return False
            number //= 10
        return True
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numbers = []
        for i in range(left, right + 1):
            if (self.selfDividingCheck(i)):
                numbers.append(i)
        return numbers
                