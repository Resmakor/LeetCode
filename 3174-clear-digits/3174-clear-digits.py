class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        while True:
            i = 0
            while i < len(s):
                if s[i] >= '0' and s[i] <= '9':
                    for j in range(i - 1, -1, -1):
                        if s[j] < '0' or s[j] > '9':
                            s = s[0:j] + s[j + 1: i] + s[i + 1:]
                            i = 0
                            break
                i += 1
            return s