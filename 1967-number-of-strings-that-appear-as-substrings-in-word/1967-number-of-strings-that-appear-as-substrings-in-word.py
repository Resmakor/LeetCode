class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        output = 0
        for pattern in patterns:
            if pattern in word:
                output += 1
        return output