class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        s_size = len(s)
        for i in range(s_size - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score