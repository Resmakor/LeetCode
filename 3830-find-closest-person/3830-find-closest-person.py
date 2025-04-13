class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        dist_1 = abs(x - z)
        dist_2 = abs(y - z)
        if dist_1 == dist_2:
            return 0
        elif dist_1 > dist_2:
            return 2
        return 1