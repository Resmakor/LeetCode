class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        needed_rows = [] 
        value_position = 0 
        for index, row in enumerate(self.grid):
            if value in row:
                value_position = row.index(value)
                if index - 1 >= 0:
                    needed_rows.append(self.grid[index - 1])
                needed_rows.append(row)
                if index + 1 < len(self.grid):
                    needed_rows.append(self.grid[index + 1])
                break
        output = 0
        for row in needed_rows:
            if value in row:
                if value_position - 1 >= 0 and value_position + 1 < len(row):
                    output += row[value_position - 1] + row[value_position + 1]
                if value_position - 1 < 0:
                    output += row[value_position + 1]
                if value_position + 1 >= len(row):
                    output += row[value_position - 1]
            else:
                output += row[value_position]
        return output
    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        needed_rows = [] 
        value_position = 0 
        for index, row in enumerate(self.grid):
            if value in row:
                value_position = row.index(value)
                if index - 1 >= 0:
                    needed_rows.append(self.grid[index - 1])
                if index + 1 < len(self.grid):
                    needed_rows.append(self.grid[index + 1])
                break
        output = 0
        for index, row in enumerate(needed_rows):
            if value_position - 1 >= 0:
                output += row[value_position - 1]
            if value_position + 1 < len(row):
                output += row[value_position + 1]  
        return output
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)