class Solution(object):
    def __init__(self):
        self.board = [[""] * 3 for _ in range(3)]
    def isOver(self, moves):
        for i in range(3):
            if self.board[i][0] and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[1][1] and ((self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] == self.board[2][0])):
            return self.board[1][1]
        if len(moves) == 9: 
            return 'Draw'
        return 'Pending'
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        is_A = True
        for row, column in moves:
            if is_A:
                self.board[row][column] = 'A'
            else:
                self.board[row][column] = 'B'
            is_A = not is_A
        return self.isOver(moves)