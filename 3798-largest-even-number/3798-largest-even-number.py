class Solution:
    def largestEven(self, s: str) -> str:
        while len(s) > 0:
            if int(s[-1]) % 2 == 1:
                s = s[:len(s) - 1]
            else:
                return s
        return s

