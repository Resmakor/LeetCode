import math
class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        output = 0
        for x in range(limit + 1):
            for y in range(limit + 1):
                for z in range(limit + 1):
                    if x + y + z == n:
                        output += 1
        return output
            
        