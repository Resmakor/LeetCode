class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        coord1 = ord(coordinate1[0]) + ord(coordinate1[1])
        coord2 = ord(coordinate2[0]) + ord(coordinate2[1])
        return coord1 % 2 == coord2 % 2