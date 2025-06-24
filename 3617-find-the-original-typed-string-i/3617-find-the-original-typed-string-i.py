class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        output = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                output += 1
        return output