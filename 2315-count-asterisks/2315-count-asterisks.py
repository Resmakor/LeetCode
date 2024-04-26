class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split("|")
        output = 0
        for i in range(0, len(s), 2):
            asteriks = s[i].count("*")
            output += asteriks
        return output