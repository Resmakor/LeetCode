class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        for index, element in enumerate(str(n)):
            if index % 2 == 0:
                output += int(element)
            else:
                output -= int(element)
        return output