class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        for element in grid:
            negative = [number for number in element if number < 0]
            output += len(negative)
        return output