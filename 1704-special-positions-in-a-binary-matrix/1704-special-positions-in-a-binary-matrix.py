class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        output = 0
        row_sum = [sum(row) for row in mat]
        column_sum = [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
        print(column_sum)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_sum[i] == 1 and column_sum[j] == 1:
                    output += 1
        return output