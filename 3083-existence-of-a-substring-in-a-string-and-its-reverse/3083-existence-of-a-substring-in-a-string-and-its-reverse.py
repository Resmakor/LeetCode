class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed_s = s[::-1]
        s_size = len(s)
        for i in range(s_size - 1):
            if s[i] + s[i + 1] in reversed_s:
                return True
        return False