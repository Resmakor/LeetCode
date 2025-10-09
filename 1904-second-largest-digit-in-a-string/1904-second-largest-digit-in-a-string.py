class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = []
        for char in s:
            if char >= '0' and char <= '9':
                digits.append(int(char))
        digits = list(set(digits))
        if len(digits) < 2:
            return -1
        digits = sorted(digits)
        return digits[-2]