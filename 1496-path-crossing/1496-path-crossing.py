class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        current_point, visited_points  = [0, 0], [[0, 0]]
        for command in path:
            if command == 'N':
                current_point[1] += 1
            elif command == 'S':
                current_point[1] -= 1
            elif command == 'E':
                current_point[0] += 1
            elif command == 'W':
                current_point[0] -= 1
            if current_point in visited_points:
                return True
            visited_points.append([current_point[0], current_point[1]])
        return False