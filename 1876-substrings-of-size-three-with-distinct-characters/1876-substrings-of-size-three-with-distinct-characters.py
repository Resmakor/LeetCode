class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        string_size = len(s)
        for i in range(string_size - 2):
            substring = s[i: i + 3]
            if len(set(substring)) == len(list(substring)):
                output += 1
        return output