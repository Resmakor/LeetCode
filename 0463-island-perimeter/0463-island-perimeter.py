class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    if i == 0 or not grid[i - 1][j]:
                        output += 1
                    if i == len(grid) - 1 or not grid[i + 1][j]:
                        output += 1
                    if j == 0 or not grid[i][j  - 1]:
                        output += 1
                    if j == len(grid[i]) - 1 or not grid[i][j + 1]:
                        output += 1
        return output