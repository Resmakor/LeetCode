class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        area_sqrt = int(sqrt(area))
        for i in range(area_sqrt, 0, -1):
            if area % i == 0:
                return [area // i, i]