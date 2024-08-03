class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lower()
        counter = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                counter += 1
        return counter