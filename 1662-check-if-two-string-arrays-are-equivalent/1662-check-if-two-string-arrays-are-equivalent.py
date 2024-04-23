class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1_str = ''.join(word1)
        word2_str = ''.join(word2)
        return word1_str == word2_str