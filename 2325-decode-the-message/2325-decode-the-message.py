import string
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        letters = list(string.ascii_lowercase)
        alphabet = {
        }
        counter = 0
        key = key.replace(' ', '')
        for letter in key:
            if letter not in alphabet.keys():
                alphabet[letter] = letters[counter]
                counter += 1
            
        output = ""
        counter = 0
        for letter in message:
            if letter in alphabet.keys():
                output += alphabet[letter]
            else:
                output += letter
        return output