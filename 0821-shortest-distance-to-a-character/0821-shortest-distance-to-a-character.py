class Solution(object):
    def minIndex(self, index, e_indexes):
        minimum = abs(index - e_indexes[-1])
        for element in e_indexes:
            if abs(index - element) < minimum:
                minimum = abs(index - element)
        return minimum
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        output = []
        e_indexes = [i for i in range(len(s)) if s[i] == c]
        for i in range(len(s)):
            output.append(self.minIndex(i, e_indexes))
        return output