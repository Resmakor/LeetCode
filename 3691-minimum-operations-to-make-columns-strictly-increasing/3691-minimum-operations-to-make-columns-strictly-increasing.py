class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] <= grid[i - 1][j]:
                    output += (grid[i - 1][j] - grid[i][j]) + 1
                    grid[i][j] += (grid[i - 1][j] - grid[i][j]) + 1
        return output
        