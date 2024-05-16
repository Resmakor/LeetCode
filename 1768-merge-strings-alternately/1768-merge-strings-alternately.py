class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        min_size = min(len(word1), len(word2))
        for i in range(min_size):
            output += word1[i] + word2[i]
        if len(word1) <= len(word2):
            return output + word2[min_size:]
        return output + word1[min_size:]