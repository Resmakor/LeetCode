class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(len(grid) - 2):
            max_row = []
            for j in range(len(grid[0]) - 2):
                maximum = max(grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3])
                max_row.append(maximum)
            output.append(max_row)
        return output