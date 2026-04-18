class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        A_X = points[0][0]
        A_Y = points[0][1]
        B_X = points[1][0]
        B_Y = points[1][1]
        C_X = points[2][0]
        C_Y = points[2][1]
        return not (B_Y - A_Y)*(C_X - B_X) == (C_Y - B_Y) * (B_X - A_X)