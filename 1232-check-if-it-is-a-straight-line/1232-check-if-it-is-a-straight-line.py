class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0
        for i in range(2, len(coordinates)):
            curr_x, curr_y = coordinates[i]
            curr_dx = curr_x - x0
            curr_dy = curr_y - y0
            if dy * curr_dx != dx * curr_dy:
                return False
        return True