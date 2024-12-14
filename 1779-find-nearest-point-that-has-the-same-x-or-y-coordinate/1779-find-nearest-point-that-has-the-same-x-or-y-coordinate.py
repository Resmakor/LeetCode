class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        minimum = [-1, -1]
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                current_distance = abs(x - points[i][0]) + abs(y - points[i][1])
                if minimum == [-1, -1]:
                    minimum = [current_distance, i]
                if current_distance < minimum[0]:
                    minimum = [current_distance, i]
        if minimum != [-1]:
            return minimum[1]
        return -1
                