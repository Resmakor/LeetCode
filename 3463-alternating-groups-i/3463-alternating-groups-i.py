class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        output = 0
        for i in range(len(colors)):
            if colors[i - 1] != colors[i] and colors[(i + 1) % len(colors)] != colors[i]:
                output += 1
        return output