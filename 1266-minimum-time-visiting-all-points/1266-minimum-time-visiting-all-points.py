class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        output = 0
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
            
            x_difference = abs(next_point[0] - current_point[0])
            y_difference = abs(next_point[1] - current_point[1])
            
            output += max(x_difference, y_difference)
        return output