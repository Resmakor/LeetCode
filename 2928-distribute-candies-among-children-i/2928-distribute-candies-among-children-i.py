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
                z = n - x - y
                if x + y + z == n and z >= 0 and z <= limit:
                        output += 1
        return output
            
        