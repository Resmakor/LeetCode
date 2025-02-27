class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        output = 0
        row, column = 0, 0
        for i in range(len(board)):
            if 'R' in board[i]:
                row, column = i, board[i].index('R')
        # Left
        pointer = column - 1
        while pointer >= 0:
            if board[row][pointer] == 'B':
                break         
            elif board[row][pointer] == 'p':
                output += 1
                break
            else:
                pointer -= 1
        # Right
        pointer = column + 1
        while pointer < len(board[row]):
            if board[row][pointer] == 'B':
                break         
            elif board[row][pointer] == 'p':
                output += 1
                break
            else:
                pointer += 1
        # Up
        pointer = row - 1
        while pointer >= 0:
            if board[pointer][column] == 'B':
                break         
            elif board[pointer][column] == 'p':
                output += 1
                break
            else:
                pointer -= 1
        # Down
        pointer = row + 1
        while pointer < len(board):
            if board[pointer][column] == 'B':
                break         
            elif board[pointer][column] == 'p':
                output += 1
                break
            else:
                pointer += 1
        return output
        