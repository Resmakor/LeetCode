class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        output = 0
        for i in range(len(s)):
            output += abs(i - t.index(s[i]))
        return output
            