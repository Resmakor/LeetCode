from collections import Counter
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_counter, consonants_counter = 0, 0
        dictionary = Counter(s)
        for letter in s:
            if letter in vowels:
                if dictionary[letter] > vowels_counter:
                    vowels_counter = dictionary[letter]
            else:
                if dictionary[letter] > consonants_counter:
                    consonants_counter = dictionary[letter]
        return vowels_counter + consonants_counter