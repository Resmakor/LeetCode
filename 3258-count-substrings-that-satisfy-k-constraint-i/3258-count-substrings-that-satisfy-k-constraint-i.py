class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        output = 0
        for i in range(n):
            zeroes, ones = 0, 0
            for j in range(i, n):
                if s[j] == '0':
                    zeroes += 1
                else:
                    ones += 1
                if zeroes <= k or ones <= k:
                    output += 1
        return output