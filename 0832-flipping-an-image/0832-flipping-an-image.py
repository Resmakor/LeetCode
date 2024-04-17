class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in image:
            new_row = []
            row.reverse()
            for element in row:
                new_row.append(int(not element))
            result.append(new_row)
        return result 