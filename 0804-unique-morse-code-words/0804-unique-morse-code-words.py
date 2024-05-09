import string
class Solution(object):
    def __init__(self):
        self.morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.morse_alphabet = {}
    def transform(self, word):
        output = ""
        for character in word:
            output += self.morse_alphabet[character]
        return output
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        output_list = []
        alphabet_list = list(string.ascii_lowercase)
        for i in range(len(alphabet_list)):
            self.morse_alphabet[alphabet_list[i]] = self.morse_list[i]
        for word in words:
            output_list.append(self.transform(word))
        return len(set(output_list))