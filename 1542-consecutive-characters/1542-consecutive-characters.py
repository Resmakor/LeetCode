class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        current, maxim = 1, 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                current += 1
            else:
                if maxim < current:
                    maxim = current
                current = 1
        if current > maxim:
            return current
        return maxim