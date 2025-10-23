class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_score = 0
        for char in s:
            s_score += ord(char) - 96
        for i in range(len(s)):
            if i == 0:
                L = ord(s[0]) - 96
                R = s_score - L
            else:
                R -= ord(s[i]) - 96
                L += ord(s[i]) - 96
            if L == R:
                return True
        return False
