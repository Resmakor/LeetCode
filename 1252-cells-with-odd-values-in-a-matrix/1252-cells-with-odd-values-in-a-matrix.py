class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for indice in indices:
            for i in range(len(matrix[indice[0]])):
                matrix[indice[0]][i] += 1
            for i in range(len(matrix)):
                matrix[i][indice[1]] += 1
        output = 0
        for row in matrix:
            output += len([element for element in row if element % 2 != 0])
        return output