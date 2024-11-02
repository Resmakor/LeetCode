class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            if grid[i].count(1) == len(grid[i]) - 1:
                return i
                    