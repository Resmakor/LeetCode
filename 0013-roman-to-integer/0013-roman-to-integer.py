class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        integer = 0
        for i in range(len(s)):
            if i > 0:
                if alphabet[s[i]] > alphabet[s[i - 1]]:
                    integer += alphabet[s[i]] - 2 * alphabet[s[i - 1]]
                else:
                    integer += alphabet[s[i]]
            else:
                integer += alphabet[s[i]]
        return integer
                
            