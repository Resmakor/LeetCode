import string
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = list(string.ascii_lowercase)
        output = ""
        i = len(s)
        while i > 0 :
            if s[i - 1] == '#':
                output += alphabet[int(s[i - 3] + s[i - 2]) - 1]
                i -= 2
            else:
                output += alphabet[int(s[i - 1]) - 1]
            i -= 1
        return output[::-1]
        