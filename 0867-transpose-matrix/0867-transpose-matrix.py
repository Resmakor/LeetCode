class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(len(matrix[0])):
            temp_list = []
            for j in range(len(matrix)):
                temp_list.append(matrix[j][i])
            output.append(temp_list)
        return output