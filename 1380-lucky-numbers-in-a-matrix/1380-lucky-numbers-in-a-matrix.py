class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_row = [min(element) for element in matrix]
        output = []
        for i in range(len(matrix[0])):
            temp_max = 0
            for j in range(len(matrix)):
                if matrix[j][i] > temp_max:
                    temp_max = matrix[j][i]
                    index = j
            if temp_max != 0 and min_row[index] == temp_max:
                output.append(temp_max)
        return output
                    
                
            