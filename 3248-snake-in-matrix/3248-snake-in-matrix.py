class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        matrix, counter = [], 0
        for i in range(n):
            temp_list = []
            for j in range(n):
                temp_list.append(counter)
                counter += 1
            matrix.append(temp_list)
        i, j = 0, 0
        for command in commands:
            if command == "UP":
                i -= 1
            if command == "DOWN":
                i += 1
            if command == "RIGHT":
                j += 1
            if command == "LEFT":
                j -= 1
        return matrix[i][j]