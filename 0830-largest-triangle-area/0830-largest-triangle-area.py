class Solution(object):
    def area(self, point_1, point_2, point_3):
        a = point_1[0] * (point_2[1] - point_3[1])
        b = point_2[0] * (point_3[1] - point_1[1])
        c = point_3[0] * (point_1[1] - point_2[1])
        return 0.5 * abs(a + b + c)
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        output = -1
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    curr_area = self.area(points[i], points[j], points[k])
                    if output < curr_area:
                        output = curr_area
        return output