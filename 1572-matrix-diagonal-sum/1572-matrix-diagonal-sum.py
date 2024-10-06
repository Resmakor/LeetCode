class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        output = 0
        mat_size = len(mat)
        for i in range(mat_size):
            output += mat[i][i] + mat[i][mat_size - i - 1]
        if mat_size % 2 == 1:
            output -= mat[mat_size // 2][mat_size // 2]
        return output