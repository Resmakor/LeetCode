class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        output = 0
        for i in range(1, min(a,b) + 1):
            if a % i == 0 and b % i == 0:
                output += 1
        return output