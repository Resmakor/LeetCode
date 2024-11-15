class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m * n != len(original):
            return []
        output = []
        counter = 0
        for i in range(m):
            temp_list = []
            for j in range(n):
                temp_list.append(original[counter])
                counter += 1
            output.append(temp_list)
        return output