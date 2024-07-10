class Solution(object):
    def __init__(self):
        self.x = 0
        self.y = 0
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        for move in moves:
            if move == 'R':
                self.x += 1
            elif move == 'L':
                self.x -= 1
            elif move == 'U':
                self.y += 1
            elif move == 'D':
                self.y -= 1
        return self.x == 0 and self.y == 0
        