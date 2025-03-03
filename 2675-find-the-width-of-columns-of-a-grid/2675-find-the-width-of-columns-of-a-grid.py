class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        output = []
        for i in range(len(grid[0])):
            maxim = pow(10, -9)
            for row in grid:
                maxim = max(len(str(row[i])), maxim)
            output.append(maxim)
        return output