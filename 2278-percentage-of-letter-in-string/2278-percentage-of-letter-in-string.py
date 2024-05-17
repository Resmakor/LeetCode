class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        counter = float(s.count(letter))
        size = float(len(s))
        return int(counter / size * 100)
        