class Solution(object):
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    def count_vowels(self, text):
        vow_number = 0
        for character in text:
            if character in self.vowels:
                vow_number += 1
        return vow_number
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.count_vowels(s[0:len(s) / 2]) == self.count_vowels(s[len(s) / 2:])