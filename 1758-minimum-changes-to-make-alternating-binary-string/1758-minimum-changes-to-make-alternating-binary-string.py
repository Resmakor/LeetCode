class Solution:
    def minOperations(self, s: str) -> int:
        output = 0
        i = 0
        for i in range(len(s)):
            if int(s[i]) != i % 2:
                output += 1
        return min(output, len(s) - output)
