class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        max_distance = 0
        for i in range(len(points) - 1):
            distance = points[i + 1][0] - points[i][0]
            if distance > max_distance:
                max_distance = distance
        return max_distance