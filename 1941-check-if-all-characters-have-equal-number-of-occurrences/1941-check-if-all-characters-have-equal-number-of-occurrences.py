class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {}
        for letter in s:
            dictionary[letter] = 0
        for letter in s:
            dictionary[letter] += 1
        
        for value in dictionary.values():
            if dictionary.values().count(value) != len(dictionary.values()):
                return False
            return True