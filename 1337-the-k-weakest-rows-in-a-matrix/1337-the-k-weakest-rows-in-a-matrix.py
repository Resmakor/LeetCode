class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        rows = []
        for index, row in enumerate(mat):
            rows.append([index, row.count(1)])
        sorted_rows = sorted(rows, key=lambda x: (x[1]))
        output = [element[0] for element in sorted_rows][:k]
        return output