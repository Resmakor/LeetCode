class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while True:
            previous = s
            s = s.replace('AB', '')
            s = s.replace('CD', '')
            if previous == s:
                break
        return len(s)