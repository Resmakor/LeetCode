class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        columns = []
        for i in range(len(strs[0])):
            column = ""
            for j in range(len(strs)):
                column += strs[j][i]
            columns.append(column)
        output = 0
        for element in columns:
            if list(element) != sorted(element):
                output += 1
        return output