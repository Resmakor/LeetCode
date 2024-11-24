class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = ''.join(sorted(s, reverse=True)) 
        for character in s:
            if character.isupper() and lower(character) in s:
                return character
        return ""