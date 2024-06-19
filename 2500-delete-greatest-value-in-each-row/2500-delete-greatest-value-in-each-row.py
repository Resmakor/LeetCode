class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        while len(grid[0]) != 0:
            current_max = 0
            for row in grid:
                max_row = max(row)
                if max_row > current_max:
                    current_max = max_row
                row.remove(max(row))
            output += current_max
        return output
                