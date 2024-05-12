import string
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = list(string.ascii_lowercase)
        for letter in sentence:
            try:
                alphabet.remove(letter)
            except:
                continue
        return len(alphabet) == 0