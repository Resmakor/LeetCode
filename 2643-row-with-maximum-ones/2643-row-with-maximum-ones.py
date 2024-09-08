class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        output = [0, 0]
        for index, row in enumerate(mat):
            ones = row.count(1)
            if ones > output[1]:
                output = [index, ones]
        return output
                