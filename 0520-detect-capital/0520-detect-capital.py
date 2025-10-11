class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upper = 0
        for char in word:
            if char.isupper():
                upper += 1
        if len(word) == upper or (word[0].isupper() and upper == 1) or upper == 0:
            return True
        return False
