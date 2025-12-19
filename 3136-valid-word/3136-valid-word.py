class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel = False
        consonant = False
        for char in word:
            if char >= '0' and char <= '9':
                continue
            elif char in vowels:
                vowel = True
            elif char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
                consonant = True
            else:
                return False
        return vowel and consonant