class Solution(object):
    def loop(self, s):
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return s[0:i] + s[i + 2:]
        return s
                
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        while True:
            size = len(s)
            s = self.loop(s)
            if size == len(s):
                return s