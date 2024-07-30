class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            if i == 0:
                output.append([1])
            elif i == 1:
                output.append([1, 1])
            else:
                temp_list = []
                for j in range(len(output[-1]) - 1):
                    temp_list.append(output[-1][j] + output[-1][j + 1])
                temp_list = [1] + temp_list + [1]
                output.append(temp_list)
        return output