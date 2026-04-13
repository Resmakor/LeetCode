class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    output.append(matrix[i][j])
                else:
                    output[j] += matrix[i][j]
        return output
