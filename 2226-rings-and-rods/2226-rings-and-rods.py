class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        output = 0
        for i in range(10):
            i = str(i)
            if 'R' + i in rings and 'G' + i in rings and 'B' + i in rings:
                output += 1
        return output