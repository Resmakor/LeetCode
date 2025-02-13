class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        counter = 0
        for i in range(1, n + 1, 1):
            if n % i == 0:
                counter += 1
            if counter > 3:
                return False
        return counter == 3