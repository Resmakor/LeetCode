class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        all_numbers = set(range(1, n + 1))
        for i in range(n):
            if all_numbers != set(matrix[i]) or all_numbers != set([col[i] for col in matrix]):
                return False
        return True
