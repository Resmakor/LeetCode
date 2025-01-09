class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        output = 0
        for i in range(len(colors)):
            temp_distance = 0
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    temp_distance = abs(j - i)
                    if temp_distance > output:
                        output = temp_distance
        return output
